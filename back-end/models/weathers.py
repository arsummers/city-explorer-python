from os import environ
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
from datetime import datetime

class Forecast:
    def __init__(self, query_result):
        self.forecast = query_result['summary']
        epoch_seconds = int(query_result['time'])
        self.time = datetime.utcfromtimestamp(epoch_seconds).strftime("%A %B %d, %Y")

    def serialize(self):
        return vars(self)

    @staticmethod
    def fetch(latitude, longitude):
        WEATHER_API_KEY = environ.get('WEATHER_API_KEY')

        url = f'https://api.darksky.net/forecast/{WEATHER_API_KEY}/{latitude},{longitude}'

        forecasts = requests.get(url).json()

        dailies = [Forecast(daily).serialize() for daily in forecasts['daily']['data']]

        return json.dumps(dailies)
