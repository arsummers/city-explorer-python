
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
from flask import Flask, jsonify, request
import requests
# from back-end.models.locations import Location
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
