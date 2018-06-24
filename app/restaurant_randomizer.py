import json
import requests
import random
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("YELP_API_KEY") or "OOPS. Please set an environment variable named 'YELP_API_KEY'."

def is_valid_zip(zip_code):
    try:
        float(zip_code)
        return True
    except Exception as e:
        return False

def wrong_zip_format():
    print("Invalid zip code, please enter a zip code consisting of 5 digits.")
    quit("Please try again.")


print("WELCOME TO THE RANDOM LUNCH SELECTOR APP!")
print("-----------------------------------------")
zip_code = input("Please enter your zip code:")

if is_valid_zip(zip_code) == False:
    wrong_zip_format()

price = input("Please enter a price level between 1 and 4, (1 = cheap, 4 = very fancy): ")

if int(price) >= 4:
    print("Please enter a price level of either 1, 2, 3, or 4.")
    quit("Please try again.")


request_url = "https://api.yelp.com/v3/businesses/search?location=" + zip_code + "?radius=800?term=food?price=" + price +"?open_now"
response = requests.get(request_url, headers={"Authorization": "Bearer " + YELP_API_KEY})

response_body = json.loads(response.text)

data = response_body["businesses"]
places = list(data)

choice = random.choice(places)
choice_data = list(choice)
address = choice['location']

print("*****************************************")
print("Your restaurant choice for today is:")
print("*****************************************")
print(choice['name'])
print("Yelp rating: " + str(choice['rating']))
print("Address: " + address['address1'] + ", " + address['city'] + " " + address['state'] + " " + address['zip_code'])
print("Phone: " + (choice['display_phone']))
print("")
print("BON APPETIT!!")


#if __name__ == "__main__":
