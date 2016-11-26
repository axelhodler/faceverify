from flask import Flask
app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def verify():
  return "Hello World!"

if __name__ == "__main__":
  app.run()
