from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS


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
        GEOCODE_API_KEY = os.environ.get('GEOCODE_API_KEY')


        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GEOCODE_API_KEY}'

        locations = requests.get(url).json()

        new_location = Location(query, locations['results'][0])

        return json.dumps(new_location.serialize())

