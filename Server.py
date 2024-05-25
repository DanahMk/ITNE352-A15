
import socket
import threading
import requests
import json
import os

NEWS_API_KEY = '2d0ead31247748069c0003f6a72d8c0d'
BASE_URL = 'https://newsapi.org/v2/'
HOST = '127.0.0.1'
PORT = 65432

def fetch_news_all(endpoint, params):
    params['apiKey'] = NEWS_API_KEY
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Unnable to fetch data'}

def convertData(group_id, client_name, option, data):
    filename = f"{group_id}_{client_name}_{option}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
