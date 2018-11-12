from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
import random
import redis
import time

app = Flask(__name__)
api = Api(app)
cache = redis.Redis(host='redis', port=6379)

welcome_message = [
  'Hello, World!',
  'Welcome to my Docker project',
  'I have no idea what I\'m doing',
  'Please containerize.',
]


@api.route('/v1/message')
class Message(Resource):
  def get_hits(self):
      retries = 5
      while True:
          try:
              return cache.incr('hits')
          except redis.exceptions.ConnectionError as exc:
              if retries == 0:
                  raise exc
              retries -= 1
              time.sleep(0.5)
              
  def get(self):
    return { 'content': random.choice(welcome_message), 'hits': self.get_hits() }

if __name__ == "__main__":
  app.run()
