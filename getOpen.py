import requests
# Use google api

def search_store(latitude, longitude, query):
    api_key = 'AIzaSyDqm-LHxLt-X0qtnbMI6iotbTq1h1WwJcw'
    URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&location={}+{}&radius=1000&language=ja&key={}'

    r = requests.get(URL.format(query, latitude, longitude, api_key))
    return r.json()['results']

def make_store_info(store):
    return {

    }

def search_open_info(latitude, longitude, query):
    api_key = 'AIzaSyDqm-LHxLt-X0qtnbMI6iotbTq1h1WwJcw'
    URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&location={}+{}&radius=1000&language=ja&key={}'

    r = requests.get(URL.format(query, latitude, longitude, api_key))
    return r.json()['results'][0]['opening_hours']['open_now']

# print(search_store(longitude=135.495257, latitude=34.679193, query='お好み焼き || たこ焼き'))


address = '東京都台東区上野４－８－６　プラザUビル　B1F'
name = '完全個室肉バル ココバル coco baru 上野店'
query = address + ' ' + name
print(search_open_info(longitude=139.7738125004, latitude=35.7096797618, query=query))