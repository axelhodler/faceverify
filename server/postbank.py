import os
import requests
import json

API_KEY=os.environ['POSTBANK_API_KEY']
USERNAME=os.environ['POSTBANK_USERNAME']
PASSWORD=os.environ['POSTBANK_PASSWORD']

def get_token():
  headers= {
          "API-Key": API_KEY
          }
  data={
    'username': USERNAME,
    'password': PASSWORD
  }
  r = requests.post('https://hackathon.postbank.de/bank-api/gold/postbankid/token', headers=headers, data=data)
  return json.loads(r.text)['token']


