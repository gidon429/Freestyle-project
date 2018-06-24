# Setup Instructions

In order to use the app you will need to create an API key through Yelp's website. Create a Yelp developer account here and follow prompts to obtain an API key: https://www.yelp.com/login?return_url=%2Fdevelopers%2Fv3%2Fmanage_app.

Once created, save a file called ".env" in the same directory that the restaurant_randomizer.py file is saved and place inside the phrase: YELP_API_KEY = "Your Yelp API Key here"

If the application comes up with an error with the env approach above, simply set the API Key directly in the command line by typing in 
set YELP_API_KEY="Your Yelp API Key here"

Run the application from the command line by navigating to its directory and typing "python restaurant_randomizer.py".
It will prompt you for your zip code and price preference and return a random restaurant within half a mile of the center of the zip code area.
