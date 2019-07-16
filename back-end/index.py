from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

# sets up the port, allows it to access from the hidden .env file
from dotenv import load_dotenv
load_dotenv()

# used to access items in my hidden .env file. Keeping these global so they can be easily accessed below as needed.
PORT = os.getenv('PORT')
GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')

# builds from both classes in the class demo - if I incorporate more APIS, I will have more classes.
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



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)


        if parsed_path.path == '/locations':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            parsed_query_string = parse_qs(parsed_path.query)

            # helps clean up the response
            query = parsed_query_string['data'][0]

            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GEOCODE_API_KEY}'
            location = Locations(url, query)
            print('geocode url', url)

            result = requests.get(url).json()

            formatted_query = result['results'][0]['formatted_address']

            print('formatted query: ', formatted_query)

            # the indent helps with the formatting - instead of getting a long line of json objects, they'll be nicely organized onto their own lines. The sort_keys puts everything into alphabetical order
            json_string = json.dumps(location.serialize(), indent=4, sort_keys=True)

            print(json_string.encode())
            self.wfile.write(json_string.encode())
            return

        self.send_response_only(404)
        self.end_headers()


# create server environment
def create_server():
    return HTTPServer(
        # since PORT is a variable in my .env, and it is read as a string, since Python doesn't have the same level of type coercion as javascript, I've turned it into an integer to keep the port running
        ('127.0.0.1', int(PORT)), SimpleHTTPRequestHandler
    )

def run_forever():
    server = create_server()

    try:
        print(f'Starting server on Port {PORT}')
        server.serve_forever()

    except:
        KeyboardInterrupt
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()


