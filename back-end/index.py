from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()



class Locations():
    def __init__(self, url, query):
        self.url = url
        self.get_data_for_location(url)


    def get_data_for_location(self, url):
        result = requests.get(url).json()
        self.formatted_query = result['results'][0]['formatted_address']
        self.latitude = result['results'][0]['geometry']['location']['lat']
        self.longitude = result['results'][0]['geometry']['location']['lng']


    def serialize(self):
        return vars(self)



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        print('request path', parsed_path)
        print('parsed query', parse_qs)

        if parsed_path.path == '/locations':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()


            # used to access the geocode API key in my hidden .env file
            GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')

            parsed_query_string = parse_qs(parsed_path.query)
            query = parsed_query_string['data'][0]
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GEOCODE_API_KEY}'
            location = Locations(url, query)
            print('geocode url', url)

            result = requests.get(url).json()

            formatted_query = result['results'][0]['formatted_address']

            print('formatted query: ', formatted_query)

            json_string = json.dumps(location.serialize())
            print(json_string.encode())
            self.wfile.write(json_string.encode())
            return

        self.send_response_only(404)
        self.end_headers()





# create server environment
def create_server():
    return HTTPServer(
        ('127.0.0.1', 3000), SimpleHTTPRequestHandler
    )

def run_forever():
    server = create_server()

    try:
        print('Starting server on Port 3000')
        server.serve_forever()

    except:
        KeyboardInterrupt
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()


