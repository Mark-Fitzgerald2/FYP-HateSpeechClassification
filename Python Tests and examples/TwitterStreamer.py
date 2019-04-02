import tweepy
import csv
from emojiToText import emojiToText
import unicodedata

class TwitterStreamer(object):

	def main(self):
		api = self.getTweepyApi()
		query = input("Do you want to search for tweet Id's, read tweets by hashtag or read by user Id? ")
		queryCorrect = False
		while(not queryCorrect):
			if query.lower() == 'tweetid':
				self.checkId(api)
				queryCorrect = True
			elif query.lower() == 'hashtag':
				self.readHashtag(api)
				queryCorrect = True
			elif query.lower() == 'userid':
				self.readUserAccount(api)
				queryCorrect = True
			else:
				query = input("Please try again and use tweetId, hashtag or userId as your response. ")
		
		#print(results)
	def getTweepyApi(self):
		CONSUMER_KEY = ''
		CONSUMER_SECRET = ''
		ACCESS_TOKEN = ''
		ACCESS_TOKEN_SECRET = ''

		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)
		return api

	def checkId(self, api):
		results = []
		file = input("What file contains the tweet Id's? ")
		with open(file, 'r', encoding='utf-8-sig') as csvfile:
			reader = csv.reader(csvfile)
			dataset = list(reader)
			i = 0
			for row in dataset:
				if len(row[0]) > 1:
					results.append(int(row[0][:-8]))
			print(results)
			#i = 1084178218805006337
			#results.append(int(dataset[1571][0][:-1]))
			#results.append(1084148836589887494)
		#print(results)
		#print(results[0] - i)
		
		noTweet = 0
		#i = 0
		arr = []
		for result in results:
			try:
				tweet = api.get_status(result)
				#print(tweet.text)
				#print(tweet.full_text)
				emojiTweet = emojiToText().demojize(tweet.text)
				print(emojiTweet)
				arr.append([emojiTweet])
				#i += 1
				#print(i)
			except:
				noTweet += 1
				#i += 1
				#print(i)
		if len(arr) > 0:
			file = input("What file do you want to write the solution to? ")
			myFile = open(file, 'w', newline='', encoding='utf-8') 	
			with myFile:  
				writer = csv.writer(myFile)
				writer.writerows(arr)
		print("The number of tweets deleted was: ", noTweet)
		
	def readHashtag(self, api):
		hashtag = input("What hashtag would you like to search for? ")
		numTweets = eval(input("How many tweets would you like to serch for? "))
		tweets = tweepy.Cursor(api.search, q=hashtag, tweet_mode='extended', lang = 'en').items(numTweets)
		arr = []
		for tweet in tweets:
			if (not tweet.retweeted) and ('RT @' not in tweet.full_text):

				emojiTweet = emojiToText().demojize(tweet.full_text)
				print(emojiTweet)
				arr.append([unicodedata.normalize('NFKD', tweet.full_text).encode('ascii','ignore')])#emojiTweet])

		file = input("What file do you want to write the solution to? ")
		myFile = open(file, 'w', newline='', encoding='utf-8') 	
		with myFile:  
			writer = csv.writer(myFile)
			writer.writerows(arr)

	def readUserAccount(self, api):
		userId = input("What user Id do you want to search for? ")
		numTweets = eval(input("How many tweets would you like to serch for? "))
		tweets = tweepy.Cursor(api.user_timeline,id=userId, tweet_mode='extended', lang = 'en').items(numTweets)
		arr = []
		for tweet in tweets:
			if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
				emojiTweet = emojiToText().demojize(tweet.full_text)
				print(emojiTweet)
				arr.append([emojiTweet])#unicodedata.normalize('NFKD', tweet.full_text).encode('ascii','ignore')])#emojiTweet])
			

		file = input("What file do you want to write the solution to? ")
		myFile = open(file, 'w', newline='', encoding='utf-8') 	
		with myFile:  
			writer = csv.writer(myFile)
			writer.writerows(arr)

	if __name__ == '__main__':
	    main()