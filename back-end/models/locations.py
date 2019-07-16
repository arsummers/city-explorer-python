from os import environ
import json
import requests

class Locations():
    def __init__(self, url, query):
        self.url = url
        self.get_data_for_location(url)
        self.search_query = query


    def get_data_for_location(self, url):
        result = requests.get(url).json()

        # Digs into the JSON object the API gave back to me via postman
        # Works a lot like the dot notation I used to dig into the same API when I did city explorer in javascript
        # JSON comes out looking like a dictionary full of lists, so I was able to access it like able to access it like I would a dictionary full of lists.


        self.formatted_query = result['results'][0]['formatted_address']

        self.latitude = result['results'][0]['geometry']['location']['lat']

        self.longitude = result['results'][0]['geometry']['location']['lng']


    def serialize(self):
        return vars(self)
