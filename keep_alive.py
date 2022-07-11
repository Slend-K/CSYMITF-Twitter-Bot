from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Twitter bot alive\nhttps://www.twitter.com/UMadeItToFriday"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

print("keep_alive.py fully loaded; webhook up.")