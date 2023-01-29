from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/flask')
def hello_sample():
  return "Hello flask."

@app.route('/user/<user_id>')
def hello_person(user_id):
  return "Hello " + user_id

if __name__ == '__main__':
  app.run()