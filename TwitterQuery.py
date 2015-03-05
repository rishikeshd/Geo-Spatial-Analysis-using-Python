############################################
#Using package 'tweepy' to extract data from Twitter API for geolocated tweets
#Gelocated tweets are based on a bounding box which is mentioned in the script

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import time
import json

global g_filename
consumer_key="xxxx"
consumer_secret="xxxx"
access_token="xxxx"
access_token_secret="xxxx"

class StdOutListener(StreamListener):
    def on_data(self, data):
        now = datetime.datetime.now()
        current_date=now.strftime("%m%d%Y")
        end_date='08312014'
        while end_date!=current_date:
            c_date=now.strftime("%m%d%Y")
            g_filename=str(c_date)+".json"
            with open(str(g_filename),"a") as out_file:
                json.dump(data,out_file)
        #print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #stream.filter(locations=[-6.66461,-65.47852,-18.64625,-51.94336,-4.30259,-39.72656,0.70311,-55.37109])
    stream.filter(locations=[-74,40,-73,41,-122.75,36.8,-121.75,37.8])
