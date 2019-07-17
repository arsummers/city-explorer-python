import os
import json
from flask import Flask, jsonify, request
import requests
from .models.locations import Location
from .models.weathers import Forecast
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/location', methods=['GET'])
def new_location():

    query_name = request.args.get('data')
    data = Location.fetch(query_name)
    return data




@app.route('/weather', methods=['GET'])
def weather():

    latitude = request.args.get('data[latitude]')
    print(f'*********INIT LATITUDE {latitude} *********************')
    # print(f'***************************REQUEST ARGS {request.args}')

    longitude = request.args.get('data[longitude]')


    return Forecast.fetch_weather(latitude, longitude)