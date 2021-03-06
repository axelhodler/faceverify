from flask import Flask, request, Response
from postbank import refund_deposit, deposit_payment
from face_api import participants_match
from participants import add_participant, fetch_participant
import requests
import json
import os

app = Flask(__name__)

# Yaas secret
YAAS_SECRET  = os.environ['YAAS_SECRET']
# global event url
EVENTS_URL = 'https://api.beta.yaas.io/hybris/document/v1/verifyface/verifyface.verify/data/events'

def add_preflight_headers(resp):
  resp.headers['Access-Control-Allow-Origin'] = '*'
  resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
  return resp

def get_yaas_token():
  tokenurl = 'https://api.beta.yaas.io/hybris/oauth2/v1/token'
  headers = {
          'Content-Type': 'application/x-www-form-urlencoded'
          }
  parameters = 'grant_type=client_credentials&client_id=dyST3bvNfU2MWakywYTXDXitZy7gW0HQ&client_secret=' + YAAS_SECRET + '&scope=hybris.document_view hybris.document_manage'
  r = requests.post(tokenurl, headers=headers, data=parameters)
  return json.loads(r.text)['access_token']

@app.route('/events', methods=['GET'])
def get_events():
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  resp = Response(requests.get(EVENTS_URL, headers=headers).text)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

@app.route('/events/<eventId>', methods=['GET'])
def get_event(eventId):
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  resp = Response(requests.get(EVENTS_URL + '/' + eventId, headers=headers).text)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

@app.route('/events/<eventId>/book', methods=['POST', 'OPTIONS'])
def book_event(eventId):
  resp = Response("")
  if request.method == 'OPTIONS':
    return add_preflight_headers(resp)
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  data = '{"registered": true}'
  resp = Response(requests.put(EVENTS_URL + '/' + eventId + '?patch=true', headers=headers, data=data).text)
  if request.data == '':
    print 'satoshipay'
  else:
    deposit_payment(extract_username(request), extract_password(request))
  return add_preflight_headers(resp)

@app.route('/events/<eventId>/cancel', methods=['POST', 'OPTIONS'])
def cancel_event(eventId):
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  data = '{"registered": false}'
  resp = Response(requests.put(EVENTS_URL + '/' + eventId + '?patch=true', headers=headers, data=data).text)
  refund_deposit()
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

def extract(request, key):
  return str(json.loads(request.data)[key])

def extract_password(request):
  return extract(request, 'password')

def extract_username(request):
  return extract(request, 'username')

def extract_base64_encoded_image(request):
  return extract(request, 'image')

@app.route('/events/<eventId>/verify', methods=['POST', 'OPTIONS'])
def verify_participation(eventId):
  resp = Response("")
  if request.method == 'OPTIONS':
    return add_preflight_headers(resp)
  img_src = extract_base64_encoded_image(request)
  match = participants_match(img_src, fetch_participant())
  resp = Response("false")
  if match:
    refund_deposit()
    resp = Response("true")
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

@app.route('/users', methods=['POST', 'OPTIONS'])
def register_user():
  resp = Response("")
  if request.method == 'OPTIONS':
    return add_preflight_headers(resp)
  img_src = extract_base64_encoded_image(request)
  add_participant(img_src)
  return add_preflight_headers(resp)

if __name__ == "__main__":
  app.run()
