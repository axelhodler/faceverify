import os
import requests
import json

API_KEY=os.environ['POSTBANK_API_KEY']
USERNAME=os.environ['POSTBANK_USERNAME']
PASSWORD=os.environ['POSTBANK_PASSWORD']
USERNAME_ORGA=os.environ['POSTBANK_ORGA_USERNAME']

COST=str(10)

def get_token(username):
  headers= {
          "API-Key": API_KEY
          }
  data={
    'username': username,
    'password': PASSWORD
  }
  r = requests.post('https://hackathon.postbank.de/bank-api/gold/postbankid/token', headers=headers, data=data)
  return json.loads(r.text)['token']

def extract_finalize_url(response):
  return json.loads(response)['links'][0]['href']

def finalize_deposit_payment(finalization_url, username):
  headers= {
    "API-Key": API_KEY,
    "x-auth": get_token(username),
    "Content-Type":"application/json"
  }
  r = requests.get(finalization_url, headers=headers)

# Mario (Attendee) to Mariu (Event Organizer)
def deposit_payment():
  headers= {
    "API-Key": API_KEY,
    "x-auth": get_token(USERNAME),
    "Content-Type":"application/json"
  }
  data='{"authorizationDevice": {"identifier": "668357","method": "bestSign","numberOfFailedAttempts": 0,"authorizationState": "SELECTED", "preferred": false, "aliasName": "HackathonNov01_8" }, "state": null, "creditTransfer": { "amount": ' + COST + ', "recipient": { "iban": "DE18100100100005616140", "paymentName": "Mariu Freudeafdd", "accountHolder": "Mariu Freudeafdd" }, "sender": { "iban": "DE44100100100005571149", "paymentName": "Mario Liebeafdk", "accountHolder": "Mario Liebeafd" }, "bookingDate": 1480175147919 }}'
  r = requests.post('https://hackathon.postbank.de:443/bank-api/gold/postbankid/credittransfer', headers=headers, data=data)
  finalizing_url = extract_finalize_url(r.text)
  finalize_deposit_payment(finalizing_url, USERNAME)

# Mariu (Event Organizer) gives Mario (Attendee) his money back
def refund_deposit():
  headers= {
    "API-Key": API_KEY,
    "x-auth": get_token(USERNAME_ORGA),
    "Content-Type":"application/json"
  }
  data='{"authorizationDevice": {"identifier": "668416","method": "bestSign","numberOfFailedAttempts": 0,"authorizationState": "SELECTED","preferred": false,"aliasName": "HackathonNov03_1"},"state": null,"creditTransfer": {"amount": ' + COST + ',"recipient": {"iban": "DE44100100100005571149","paymentName": "Mario Liebeafdk","accountHolder": "Mario Liebeafdk"},"sender": {"iban": "DE18100100100005616140","paymentName": "Mariu Freudeafdd","accountHolder": "Mariu Freudeafdd"},"bookingDate": 1480175147919}}'

  r = requests.post('https://hackathon.postbank.de:443/bank-api/gold/postbankid/credittransfer', headers=headers, data=data)
  finalizing_url = extract_finalize_url(r.text)
  finalize_deposit_payment(finalizing_url, USERNAME_ORGA)

