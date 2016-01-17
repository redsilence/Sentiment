from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = "rhUTo3IDEfktQcL3gz3qSM8og"
consumer_secret = "ZlAKPOO1rl1objODHcwA45qIsSMxdqOux7FJsNXXbN2k1hoI5p"


access_token = "304944155-u5BT348XsEpZgn7HldFS6WZBX2arnhPU1DxJt3It"
access_token_secret = "kzM2i4YhRs2eunEmcoT8wdomQHp2l3VEwSc1WRAkkYqC3"

track_string = 'JP Morgan'


class TweetListener(StreamListener):
    def __init__(self, file_descriptor):
        self.file_desc = file_descriptor

    def on_data(self, data):
        txt = json.loads(data)
        if 'text' in txt:
            txt = txt['text']
        txt = txt.replace('\n', ' ').replace('\r', '')
        self.file_desc.write((txt+"\n").encode("UTF-8"))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    filedesc = open("Raw_Tweets_JP_Morgan.txt", 'w')
    l = TweetListener(filedesc)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[track_string])
