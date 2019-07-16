# City Explorer (but make it snakey)
# author: Aliya Summers, Code Fellows staff

## Problem Domain
Take the solution code for the city explorer app, as it it was originally written in Code 301 in Javascript, and start converting it to Python.

# Approach

I built off the class demo to make the server, and took inspiration from my past experience with city explorer and the official javascript solution to plan out my approach to the structure of the app.

# Resources
Class demo for server building: ![here](https://github.com/codefellows/seattle-python-401d12/blob/master/class-06/demos/http-snacks/index.py)

Solution code to study and adapt: ![here](https://github.com/codefellows/seattle-python-401d12/tree/master/city-explorer-reference)

Additional info on searching and formatting JSON in python: ![coding-networker.com](https://codingnetworker.com/2015/10/python-dictionaries-json-crash-course/)


# Dependencies
http.server: BaseHTTPRequestHandler, HTTPServer
urllib.parse: urlparse, parse_qs
os
json
requests
dotenv: load_dotenv

You will also need to pipenv install dotenv and requests

# To Run Locally
Clone my code onto your computer
Get access to Google's Geocode API
Keep the API key safe in a .env file, with the variable GEOCODE_API_KEY
Set up a PORT variable in the .env

# Version
1.0.0
