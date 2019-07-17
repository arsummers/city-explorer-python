from os import environ
import json
import requests

class Location():
    def __init__(self, search_query, query_result):
        self.search_query = search_query
        self.formatted_query = query_result['formatted_address']
        self.latitude = query_result['geometry']['location']['lat']
        self.longitude = query_result['geometry']['location']['lng']


    def serialize(self):
        return vars(self)

    @staticmethod
    def fetch(query):

        """
gets the geocode data for the searched location, returns it as a json object
        """
        GEOCODE_API_KEY = environ.get('GEOCODE_API_KEY')
        # Digs into the JSON object the API gave back to me via postman
        # Works a lot like the dot notation I used to dig into the same API when I did city explorer in javascript
        # JSON comes out looking like a dictionary full of lists, so I was able to access it like able to access it like I would a dictionary full of lists.


        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GEOCODE_API_KEY}'

        locations = requests.get(url).json()

        new_location = Location(query, locations['results'][0])

        return json.dumps(new_location.serialize())
