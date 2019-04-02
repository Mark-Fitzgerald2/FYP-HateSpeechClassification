import tweepy
import csv
import emoji
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
		CONSUMER_KEY = 'uYZhhT1aOUNXZyvxz0rmI7ItX'
		CONSUMER_SECRET = 'oBQsObyE1E2ohNOIa8rvSfvNWnbZ8x5RDTOEGSUWCmYg7b9nBC'
		ACCESS_TOKEN = '1053207253547925505-GCOsjUa2zuhcId71qpsnV2UPxtjz9k'
		ACCESS_TOKEN_SECRET = 'hp7c8Vl1Ri1USxR89dPJZlBPPUHKyhfYKervnXkezUw55'

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
		i = 1
		prevJ = 0
		while(not gotTweets):
			arr = []
			j = 0
			tweets = tweepy.Cursor(self.api.user_timeline,id=self.userId, tweet_mode='extended', lang = 'en').items(self.numTweets*i)
			for tweet in tweets:
				if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
					emojiTweet = emoji.demojize(tweet.full_text)
					arr.append(emojiTweet)
					j += 1
					if j >= self.numTweets:
						gotTweets = True
						break
			if prevJ == j:
				break
			else:
				prevJ = j
			i += 1
	
		if j < self.numTweets:
			print("ERROR DID NOT GET EXACT NUMBER OF TWEETS")
			print("Instead of ", self.numTweets, ", ", j, " tweet(s) were found")	
		
		return arr