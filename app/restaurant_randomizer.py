import json
import requests
import random

def parse_response(response_text):
    if isinstance(response_text, str):
        response_text = json.loads(response_text)

    results = []
    places = response_text["businesses"]
    for business in places:
        p = business(places)
        result = {
            "name": ["name"],
            "price": ["price"],
            "address1": ["address"]
        }
        results.append(result)
    return results

API_KEY = "ACE_TLwdsFbf8fK7l0ljy7cRa-gfVjinKhOaFWnLK8M0uFM5cV-cmIdLy1D7jXIRoLKbHj95FirYwX3x-JqARpYALmveGZw2boD5pX6hTu3lJbylCIM_86oeV_wmW3Yx"

zip_code = input("Please enter your zip code:")
price = input("Please enter a price level between 1 and 4, (1 = cheap, 4 = very fancy): ")

request_url = "https://api.yelp.com/v3/businesses/search?location=" + zip_code + "?radius=800?term=food?price=" + price
response = requests.get(request_url, headers={"Authorization": "Bearer " + API_KEY})

if "LOCATION_NOT_FOUND" in response.text:
    print("Invalid zip code, please enter a zip code consisting of 5 digits.")
    quit("Please try again.")

response_body = json.loads(response.text)

data = response_body["businesses"]
places = list(data)

#restaurants = parse_response(response.text)

choice = random.choice(places)
print(choice)
