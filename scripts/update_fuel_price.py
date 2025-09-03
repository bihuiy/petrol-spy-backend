import sys
import os
import django

# Add the project directory to Python's module search path, so that I can import models Station & Price
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

# Initialize Django
django.setup()

import requests
from stations.models import Station
from prices.models import Price
import environ
from datetime import datetime


env = environ.Env()
environ.Env.read_env()


# Get access token
def get_access_token():

    get_access_token_url = (
        f'{env("API_BASE_URL")}{env("ACCESS_TOKEN_URL")}?grant_type=client_credentials'
    )
    headers = {"Authorization": env("AUTHORIZATION_HEADER")}
    res = requests.get(get_access_token_url, headers=headers)
    return res.json()["access_token"]


# Get the latest prices and update the database
def update_prices():

    update_prices_url = f'{env("API_BASE_URL")}{env("UPDATE_PRICES_URL")}'
    access_token = get_access_token()
    transaction_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    timestamp = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8",
        "apikey": env("API_KEY"),
        "transactionid": transaction_id,
        "requesttimestamp": timestamp,
    }
    res = requests.get(update_prices_url, headers=headers)
    res_data = res.json()

    # Update the stations table
    for station in res_data.get("stations", []):
        Station.objects.update_or_create(
            station_id=station["code"],
            defaults={
                "name": station.get("name"),
                "brand": station.get("brand"),
                "address": station.get("address"),
                "latitude": station["location"]["latitude"],
                "longitude": station["location"]["longitude"],
            },
        )

    # Update the prices table
    for price in res_data.get("prices", []):
        try:
            station = Station.objects.get(station_id=price["stationcode"])
            Price.objects.update_or_create(
                station=station,
                fuel_type=price["fueltype"],
                defaults={
                    "price": price["price"],
                    "last_updated": datetime.strptime(
                        price["lastupdated"], "%d/%m/%Y %H:%M:%S"
                    ),
                },
            )
        except Station.DoesNotExist:
            continue

    print("Successfully updated new fuel prices.")


if __name__ == "__main__":
    update_prices()
