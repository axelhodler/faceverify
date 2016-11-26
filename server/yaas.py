import requests
import os

YAAS_TOKEN=os.environ['YAAS_TOKEN']

def add_user(face_id):
  resource='userssamples'
  url = 'https://api.beta.yaas.io/hybris/document/v1/verifyface/verifyface.verify/data/'
  headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + YAAS_TOKEN
          }
  data = '{"face_id": "' + face_id + '" }'
  r = requests.post(url + resource, headers=headers, data=data)
  print r.text

