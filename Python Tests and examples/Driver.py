from preprocessing import preprocessing
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
from testModel import test
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt  
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import NuSVC
from sklearn.linear_model import LogisticRegression
import time
import numpy as np

class Driver(object):

	def __init__(self):	
		self.prePro = preprocessing()
		self.test = test()
		hateSpeech = pd.read_csv('C:/Users/user/OfflineDocs/FYP/Bad phrases/HateSpeech.csv', names=['Tweet', 'Hate'])
		nonHate = pd.read_csv('C:/Users/user/OfflineDocs/FYP/Good phrases/NonHatePhrases.csv', names=['Tweet', 'Hate'])
		hateSpeech.loc[hateSpeech["Hate"]=="Hate", "Hate"] = 1
		nonHate.loc[nonHate["Hate"]=="Not Hate", "Hate"] = 0
		hateSpeech_x = hateSpeech["Tweet"]
		hateSpeech_y = hateSpeech["Hate"]
		nonHate_x = nonHate["Tweet"]
		nonHate_y = nonHate["Hate"]
		nonHate_trainX, nonHate_testX, nonHate_trainY, nonHate_testY = self.test.stratifiedFolds(nonHate_x.tolist(), nonHate_y.tolist(), 3)
		hate_trainX, hate_testX, hate_trainY, hate_testY = self.test.stratifiedFolds(hateSpeech_x.tolist(), hateSpeech_y.tolist(), 3)
		self.train_X = nonHate_trainX + hate_trainX
		self.train_Y = nonHate_trainY + hate_trainY
		self.test_X = nonHate_testX + hate_testX
		self.test_Y = nonHate_testY + hate_testY

		#print(self.train_X)
		#print(self.train_Y)
		self.trainXVect = self.processTrain(self.train_X)
		self.testXVect = self.processTest(self.test_X)
		self.timeTaken = []
		self.xlabels = []
		self.Scores = []
		n_groups = 0
		for i in range(3):
			switcher = {
				0: MultinomialNB(),
				1: KNeighborsClassifier(n_neighbors = 7),
				2: RandomForestClassifier(n_estimators=100),
				3: NuSVC(gamma='scale', probability=True),
				2:LogisticRegression(solver='sag', multi_class='multinomial')
			}
			switcher2 = {
				0: "MNB",
				1: "KNN",
				2: "RF",
				3: "SVM",
				2: "LR"
			}
			t1 = time.time()
			self.main(switcher.get(i, MultinomialNB()), switcher2.get(i, "MNB"))
			t2 = time.time()
			print(switcher2.get(i, "MultinomialNB"), " time taken: {:.2f}".format(t2 - t1))
			self.timeTaken.append(t2 - t1)
			self.xlabels.append(switcher2.get(i, "MNB"))
			n_groups += 1
			self.Scores.append((self.count / len(self.pred)) * 100)
			#self.mnb = MultinomialNB()
			#self.knn = KNeighborsClassifier(n_neighbors = 7)
			#self.main()
		self.index = np.arange(n_groups)
		fig, ax = plt.subplots()
		ax.bar(self.index, self.timeTaken, 0.35)
		ax.set_xlabel('Classifiers')
		ax.set_ylabel('Time (s)')
		ax.set_title('Time Taken for Classifiers to Run')
		ax.set_xticks(self.index + 0.35 / 64)
		ax.set_xticklabels(self.xlabels)
		fig2, ax2 = plt.subplots()
		ax2.bar(self.index, self.Scores, 0.35)
		ax2.set_xlabel('Classifiers')
		ax2.set_ylabel('Accuracy (%)')
		ax2.set_title('Overall Accuracy')
		ax2.set_xticks(self.index + 0.35 / 64)
		ax2.set_xticklabels(self.xlabels)
		plt.show()

	def main(self, classifier, className):
		#self.mnb.fit(self.trainXVect, self.train_Y)
		#self.pred = self.mnb.predict(self.testXVect)
		t1Fit = time.time()
		classifier.fit(self.trainXVect, self.train_Y)
		t2Fit = time.time()
		print(className, " time taken to train: {:.2f}".format(t2Fit - t1Fit))
		t1Pred = time.time()
		self.pred = classifier.predict(self.testXVect)
		t2Pred = time.time()
		print(className, " time taken to predict: {:.2f}".format(t2Pred - t1Pred))

		self.count = 0
		for i in range(len(self.pred)):
			if self.pred[i] == self.test_Y[i]:
				self.count += 1
		#scores = cross_val_score(self.mnb, self.trainXVect, self.train_Y, cv = 10) #calculate 10 fold cross val 
		scores = cross_val_score(classifier, self.trainXVect, self.train_Y, cv = 10) 
		avg = scores.mean() #record avg result
		var = scores.std() #record std deviation 
		#self.probs = self.mnb.predict_proba(self.testXVect) #get probabilities of the classification accuracy  
		self.probs = classifier.predict_proba(self.testXVect)
		self.probsArr = []  
		#store probability of the result being positive  
		#initial array had prob of pos and neg  
		for prob in self.probs:  
			self.probsArr.append(prob[1])

		inputArr = self.train_X + self.test_X
		inputArrVect = self.processTrain(inputArr)
		outputArr = self.train_Y + self.test_Y
		labels = np.unique(outputArr); 
		print(labels)
		self.test.plot_learning_curve(classifier, 'Learning Curves (' + className + ')', inputArrVect, outputArr)

		print(className, " with overall accuracy {:.2f}%"
				.format((self.count / len(self.pred)) * 100))

		print(className, " with cross fold validation accuracy {:.2f}%, +/- {:.2f}%"
              .format(avg * 100, var * 2 * 100))

		print(self.test.confusion_matrix(self.test_Y, self.pred))
		self.test.rocCurve(self.test_Y, self.probsArr, className)

	def processTrain(self, tweets):
		return self.prePro.creatTFVector(tweets)

	def processTest(self, tweets):
		return self.prePro.transformTest(tweets)

if __name__ == '__main__':
	main()