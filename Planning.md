# Project Planning

## Problem Statement

The user needs to find an easier way to select places to eat at different times of the day. Most parts of New York have an overwhelming number of food options and it can be difficult to choose a place when several of them have good reviews and menu options. The application will use Yelp as a directory to find restaurants within the users vicinity (based on zip code) and randomly select one. If the user doesn't like the choice they can re-run the application to get another choice.
todo: describe the problem and user needs (see proposal instructions)

## Information Requirements

The application needs to know the user's location in order to narrow down search results and have enough samples to use its randomization on.

### Information Inputs

The required input will be the zip code of the user's location, to be entered in the form of integers.

### Information Outputs

The output will be a string of a restaurant's name and address.

## Technology Requirements

### APIs and Web Service Requirements

The application will use the Yelp API to carry out its searches, documentation is located at: https://www.yelp.com/developers/documentation/v3/business_search

### Python Package Requirements

The application will need the JSON application to parse the API output

### Hardware Requirements

A standard personal computer will be sufficient to run the application.
