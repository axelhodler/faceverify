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

# Mario to Mariu
def deposit_payment():
  headers= {
    "API-Key": API_KEY,
    "x-auth": get_token(),
    "Content-Type":"application/json"
  }
  data='{"authorizationDevice": {       "identifier": "668357","method": "bestSign","numberOfFailedAttempts": 0,"authorizationState": "SELECTED", "preferred": false, "aliasName": "HackathonNov01_8" }, "state": null, "creditTransfer": { "amount": 1, "recipient": { "iban": "DE18100100100005616140", "paymentName": "Mariu Freudeafdd", "accountHolder": "Mariu Freudeafdd" }, "sender": { "iban": "DE44100100100005571149", "paymentName": "Mario Liebeafdk", "accountHolder": "Mario Liebeafd" }, "bookingDate": 1480175147919 }}'
  r = requests.post('https://hackathon.postbank.de:443/bank-api/gold/postbankid/credittransfer', headers=headers, data=data)
  print json.loads(r.text)['links'][0]['href']

