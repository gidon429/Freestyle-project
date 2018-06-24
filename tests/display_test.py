import json
import requests
import random
import pytest


#request_url = "C:\Users\Gidon\Desktop\freestyle_project\testing_data\testing_data.json"

file_name = "testing_data.json"

with open(file_name, "r") as file:
    response.text = file.read()
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
