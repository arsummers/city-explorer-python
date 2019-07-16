from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()


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


