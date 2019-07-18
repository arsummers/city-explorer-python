from os import environ
import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS


class Movies():
    def __init__(self, info):
        self.title = info['results']['title']
        self.overview = info['results']['overview']
        self.average_votes = info['results']['vote_average']
        self.total_votes = info['results']['vote_count']
        self.popularity = info['results']['popularity']
        self.released_on = info['results']['release_date']

    def serialize(self):
        return vars(self)

    def fetch_movies(self, search_query):
        MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
        url = f'https://api.themoviedb.org/3/search/movie/?api_key={MOVIE_API_KEY}&language=en-US&page=1&query={search_query}'

        movies = requests.get(url).json()




