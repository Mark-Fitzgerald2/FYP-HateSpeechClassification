import tweepy
import csv
from emojiToText import emojiToText
import pickle


class streamer(object):
	
	def __init__(self, userId, numTweets):
		self.userId = userId
		self.numTweets = numTweets
		'''
		try:
			pickleIn = open("twitterApi.p", "rb")
			self.api = pickle.load(pickleIn)
		except (OSError, IOError) as e:
			self.api = self.getTweepyApi()
		'''
		self.api = self.getTweepyApi()

	def getTweepyApi(self):
		CONSUMER_KEY = ''
		CONSUMER_SECRET = ''
		ACCESS_TOKEN = ''
		ACCESS_TOKEN_SECRET = ''

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)
		'''
		pickleOut = open("twitterApi.p", "wb")
		pickle.dump(api, pickleOut)
		pickleOut.close()
		'''
		return api

	def readUserAccount(self):
		gotTweets = False
		arr = []
		i = 1
		j = 0
		while(not gotTweets):
			tweets = tweepy.Cursor(self.api.user_timeline,id=self.userId, tweet_mode='extended', lang = 'en').items(self.numTweets*i)
			
			for tweet in tweets:
				if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
					emojiTweet = emojiToText().demojize(tweet.full_text)
					arr.append(emojiTweet)
					j += 1
					if j >= self.numTweets:
						gotTweets = True
						break
			i += 1
		
		if j < self.numTweets:
			print("ERROR DID NOT GET EXACT NUMBER OF TWEETS")
			print("Instead of ", self.numTweets, ", ", j, " tweet(s) were found")	
		
		return arr