from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk
from spellchecker import SpellChecker
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

class preprocessing(object):

	def __init__(self):
		nltk.download('stopwords')
		remove = ['his', 'himself', "she's", "you've", "same", "you", "yours", "you'd", "you're", "you'll", "hers", "herself", "him", "he", "her", "she", "them"]
		self.stopWords = set(stopwords.words('english')).difference(remove)
		self.stopWords.update(["RT"])
		self.tweetTokenizer = TweetTokenizer(strip_handles=True)
		self.sbStemmer = SnowballStemmer('english')
		self.bannedSymbols = [':)', ':-)', '>:)', ':D', ':|', ':(', ':-(', '>:(', ':S']
		#self.spellcheck = SpellChecker()
		self.vectorizer = TfidfVectorizer(use_idf=False, stop_words=None, preprocessor=self.preprocessor, tokenizer=self.tokenizer)

	def checkUpperCase(self, tweet):
		words = tweet.split()
		for word in words:
			if word.isupper():
				tweet += ' ' + word.translate(str.maketrans('','',string.punctuation))
		return tweet

	def tokenizeTweet(self, tweet):
		tokenizedTweet = self.tweetTokenizer.tokenize(tweet.lower())
		#self.spellCheck(tokenizedTweet)
		return tokenizedTweet

	@staticmethod
	def stripHash(word):
		return word.lstrip("#")

	def stem(self, word):
		return self.sbStemmer.stem(word)

	def bannedWord(self, word):
		if word in self.stopWords:
			return True
		if word in self.bannedSymbols:
			return True
		
		if word.startswith(('https://', 'http://')):
			return True
		return False

	def spellCheck(self, arr):
		misspelled = self.spellcheck.unknown(arr)
		correct = self.spellcheck.known(arr)
		print(correct)
		print(misspelled)
		correctedArr = []

		for word in misspelled:
    		# Get the one most likely answer
			print(word)
			correctedArr.append(self.spellcheck.correction(word))

		for word in correct:
			correctedArr.append(word)

		print(arr)
		print(len(arr))
		print(correctedArr)
		print(len(correctedArr))

	def preprocessor(self, tweet):
		return self.checkUpperCase(tweet)

	def tokenizer(self, tweet):
		words = self.tokenizeTweet(tweet)
		stripHash = [self.stripHash(word) for word in words]
		validWords = [w for w in stripHash if not self.bannedWord(w)]

		stemm = [self.stem(word) for word in validWords]
		return stemm

	def creatTFVector(self, corpus):
		vector = self.vectorizer.fit_transform(corpus)
		pickleOut = open("vectorizer.pk", "wb")
		pickle.dump(self.vectorizer, pickleOut)
		pickleOut.close()
		return vector

	def transformTest(self, corpus):
		return self.vectorizer.transform(corpus)

	def transformText(self, corpus):
		try:
			pickleIn = open("vectorizer.pk", "rb")
			vector = pickle.load(pickleIn).transform(corpus)
			#vector = self.vectorizer.transform(corpus)
		except (OSError, IOError) as e:
			print(e)
			vector = self.vectorizer.transform(corpus)
		return vector
"""
word = "Hello"

print(word.isupper())
stopWords = set(stopwords.words('english'))
print(len(stopWords))

print(len(remove))
print(len(stopWords))
"""