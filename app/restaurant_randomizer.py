import json
import requests

access_token = "ACE_TLwdsFbf8fK7l0ljy7cRa-gfVjinKhOaFWnLK8M0uFM5cV-cmIdLy1D7jXIRoLKbHj95FirYwX3x-JqARpYALmveGZw2boD5pX6hTu3lJbylCIM_86oeV_wmW3Yx"

zip_code = input("Please enter your zip code:")



request_url = "https://api.yelp.com/v3/businesses/search?location=" + zip_code + "?radius=1600"
response = requests.get(request_url)

if "Error Message" in response.text:
    print("Invalid zip code, please enter a zip code consisting of 5 digits.")
    quit("Please try again.")

response_body = json.loads(response.text)
print(response.text)
