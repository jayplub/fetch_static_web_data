import tweepy, re, time, ConfigParser
from urllib import urlopen
from bs4 import BeautifulSoup
import re
 
config = ConfigParser.ConfigParser()
config.read('.twitter')
 
consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
while True:
    optionsUrl = 'https://www3.reg.cmu.ac.th/regist158/'
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage)
    user = str(soup.findAll('strong')[4].next)
    date_time = str(soup.findAll('b')[0].next)
    user2 = str.split(user)
    date_time2= str.split(date_time)
    print ("Useronline: "+user2[0])
    print ("time: "+date_time2[0]+"\n")
    api.update_status(status=("Useronline at CMU Student Enrollment : "+user2[0]+" "+"Users"+"\n"+"Time is now: "+date_time2[0]+"\n"+"checknow at https://www3.reg.cmu.ac.th/regist158"))
