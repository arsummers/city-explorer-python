from os import environ
import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS


class Movies():


    url = f'https://api.themoviedb.org/3/search/movie/?api_key=${MOVIE_API_KEY}&language=en-US&page=1&query=${search_query}'
    pass
