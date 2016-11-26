from flask import Flask, request, Response
import requests
import json
import os
app = Flask(__name__)

# Yaas secret
YAAS_SECRET  = os.environ['YAAS_SECRET']
# global event url
EVENTS_URL = 'https://api.beta.yaas.io/hybris/document/v1/verifyface/verifyface.verify/data/events'

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
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  data = '{"registered": true}'
  resp = Response(requests.put(EVENTS_URL + '/' + eventId + '?patch=true', headers=headers, data=data).text)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

@app.route('/events/<eventId>/cancel', methods=['POST', 'OPTIONS'])
def cancel_event(eventId):
  apitoken = get_yaas_token()
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apitoken
          }
  data = '{"registered": false}'
  resp = Response(requests.put(EVENTS_URL + '/' + eventId + '?patch=true', headers=headers, data=data).text)
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp
  
  
if __name__ == "__main__":
  app.run()  