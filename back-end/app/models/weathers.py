from os import environ
import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
from datetime import datetime


class Forecast():
    def __init__(self, info):
        self.forecast = info['summary']
        epoch_seconds = int(info['time'])
        self.time = datetime.utcfromtimestamp(epoch_seconds).strftime("%A %B %d, %Y")


    def serialize(self):
        return vars(self)

    @staticmethod
    def fetch_weather(latitude, longitude):
        # print(f'*********************************LATITUDE {latitude}****************')
        WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

        #TODO: Figure out a way to use super() functionality to access the latitude and longitude taken from the search query in locations - as long as latitude and longitude are coming up None, the rest of it won't be able to run
        # latitude = 47.6062095
        # longitude = -122.3320708
        url = f'https://api.darksky.net/forecast/{WEATHER_API_KEY}/{latitude},{longitude}'

        # print(f'************************************* WEATHER URL: {url} *********************')
        forecasts = requests.get(url).json()
        # print(f'************************************FORECAST: {forecasts} *******************')
        dailies = [Forecast(daily).serialize() for daily in forecasts['daily']['data']]

        # return jsonify(dailies)
        return json.dumps(dailies)

