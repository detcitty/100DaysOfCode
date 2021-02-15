import os
import requests
import json

KEY = os.getenv('AQS_API_KEY')
EMAIL = os.getenv('MY_EMAIL')
print(KEY)

url = ' https://aqs.epa.gov/data/api/moniters/bySite'

params = {
    'email': EMAIL,
    'key': KEY,
    'param': 'ALL',
    'bdate': 20210101,
    'edate': 20210214,
    'state': 49,
    'county': 35,
    'site': 13
}

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)

response = requests.get(url, params=params)

jprint(response.json())