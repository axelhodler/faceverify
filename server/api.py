from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def verify():
  return "Hello World!"

@app.route('/userregistrations', methods=['POST'])
def create_userregistration():
  return str(json.loads(request.data)['image'])

if __name__ == "__main__":
  app.run()
