import os
import json
from flask import Flask, jsonify, request
import requests
from .models.locations import Location, fetch_location
from .models.weathers import Forecast
from .models.movies import Movies
from .models.events import Events
from .models.trails import Trails
from .models.yelp import Yelp
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/location', methods=['GET'])
def new_location():

    saved_location = LocationsModel.query.filter_by(search_query=request.args.get('data')).first()

    if saved_location:
        return jsonify(saved_location.convert_to_dict())

    fresh_location = fetch_location()

    resource = LocationsModel(
        search_query = fresh_location.search_query,
        formatted_query = fresh_location.formatted_query,
        latitude = fresh_location.latitude,
        longitude = fresh_location.longitude
    )

    db.session.add(resource)
    db.session.commit()
    return jsonify(resource.convert_to_dict())



@app.route('/test-location-db')
def test_loc_db():

    newlocation = LocationsModel(name='seattle', formatted_query='Seattle, WA, USA', latitude=47.6062095, longitude=-122.3320708)
    db.session.add(newlocation)
    db.session.commit()

    return jsonify(newlocation.convert_to_dict())

@app.route('/api/v1/locations')
def all_locations():

    newlocation = [location.convert_to_dict() for location in LocationsModel.query.all()]
    return jsonify(newlocation)

@app.route('/weather', methods=['GET'])
def weather():

    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')

    return Forecast.fetch_weather(latitude, longitude)

@app.route('/yelp', methods=['GET'])
def yelp():
    reached_app = 'You have reached the yelp route'
    return reached_app

@app.route('/movies', methods=['GET'])
def movies():

    # title = request.args.get('info[title]')
    # overview = request.args.get('info[overview]')
    # average_votes = request.args.get('info[vote_average]')
    # total_votes = request.args.get('info[vote_count]')
    # popularity = request.args.get('info[[popularity]')
    # released_on =request.args.get('info[released_on]')

    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')

    return Movies.fetch_movies(latitude, longitude)

@app.route('/events', methods=['GET'])
def events():
    reached_app = 'You have reached the events route'
    return reached_app

@app.route('/trails', methods=['GET'])
def trails():
    reached_app = 'You have reached the trail route'
    return reached_app



from app.models.models import LocationsModel
