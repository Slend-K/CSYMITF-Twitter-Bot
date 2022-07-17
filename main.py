import tweepy
import os
import time
import schedule
import asyncio
from keep_alive import keep_alive
from datetime import date

consumer_key = os.getenv("api_key")
consumer_secret = os.getenv("api_key_secret")

api_key = os.getenv("access_token")
api_key_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(api_key, api_key_secret)

api = tweepy.API(auth)

"""
FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
  file_read = open(FILE_NAME, "r")
  last_seen_id = int(file_read.read().strip())
  file_read.close()
  return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
  file_write = open(FILE_NAME, "w")
  file_write.write(str(last_seen_id))
  file_write.close()
  return


mentions = api.mentions_timeline()


for tweet in reversed(mentions):
  api.create_favorite(tweet.id)
  time.sleep(30)
"""


def tweet():
  print("Defining 'i'")
  i = 0
  print(f"'i' defined as {i}")

  i += 1
  print(f"'i' redefined as {i}")

  print("Getting the file ready")
  upload_result = api.media_upload('video.mp4')
  print("File ready")


  print("\nCongratulating those who made it to Friday :D")
  api.update_status(status=f"Week {i} of Congratulations Sailor, You Made it to Friday!", media_ids=[upload_result.media_id_string])
  print("Congratulated\n")


schedule.every().friday.at("08:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1800)


keep_alive()