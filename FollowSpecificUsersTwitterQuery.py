###########################################################
#Using "tweepy" package to extract data from Twitter API for geolocated Tweets
#Geolocated tweets are extracted on the basis of bounding box mentioned in the script
#It also shows how to follow a specific set of users in a bounding box

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import time
import json
import string

global g_filename
consumer_key="xxxx"
consumer_secret="xxxx"
access_token="xxxx"
access_token_secret="xxxx"

class StdOutListener(StreamListener): 
    def on_data(self, data):
        now = datetime.datetime.now()
        current_date=now.strftime("%m%d%Y")
        end_date='11202014'
        while end_date!=current_date:
            c_date=now.strftime("%m%d%Y")
            g_filename=str(c_date)+".json"
            with open(str(g_filename),"a") as out_file:
                out_file.write(data)
                break
        #print data
        return True

    def on_error(self, status):
        print status

    
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #stream = Stream(auth, l)
    #stream.filter(locations=[-74.145355,40.716038,-73.928375,40.822124])
    stream = Stream(auth, l)
    array=[]
    array=[]
    with open('ids2.txt','r+') as in_file:
        for line in in_file:
            line=line.strip('\n')
            array.append(line)
    #print array[7]
    #users2 = ['194276262','355698504','2535748428']
    users = [str(u) for u in array]
    #print users
    stream.filter(follow=users,locations=[-77.110977,38.947661,-77.020683,38.971688])
    






