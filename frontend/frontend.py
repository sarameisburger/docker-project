from flask import Flask, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
  api_url = 'http://api:9001/v1/message'
  try: 
    api_message_req = requests.get(api_url, timeout=1)
    if api_message_req.status_code == 200:
      api_message = api_message_req.json()
      return '<h1>' + api_message['content'] + '</h1><br /><p>Hit counter: ' + str(api_message['hits']) + '</p>'
    else:
      return 'API at ' + api_url + ' returned error code: ' + api_message_req.status_code
  except requests.exceptions.ConnectionError:
    return 'API at ' + api_url + ' failed to connect.'

if __name__ == "__main__":
  app.run()
