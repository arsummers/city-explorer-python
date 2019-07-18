import os
import json
from flask import Flask, jsonify, request
import requests
from .models.locations import Location
from .models.weathers import Forecast
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
# check db:
    # if search name not in db, do the API stuff, insert into db
#if name in db, return the saved values

    query_name = request.args.get('data')
    data = Location.fetch(query_name)
    return data


@app.route('/testdb')
def test_loc_db():
    print('**************************************************')
    # location = LocationsModel.query.filter_by(name='seattle').first()
    newlocation = LocationsModel(name='seattle', formatted_query='Seattle, WA, USA', latitude=47.6062095, longitude=-122.3320708)
    # formatted_city = (formatted_query='Seattle, WA, USA')
    # latitude = LocationsModel(latitude=47.6062095)
    # longitude = LocationsModel(longitude=-122.3320708)

    db.session.add(newlocation)
    # db.session.add(formatted_city)
    # db.session.add(latitude)
    # db.session.add(longitude)


    db.session.commit()

    return jsonify(newlocation.convert_to_dict())



@app.route('/weather', methods=['GET'])
def weather():

    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')


    return Forecast.fetch_weather(latitude, longitude)


from app.models.models import LocationsModel
