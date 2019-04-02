import random
import math
from sklearn import metrics
import matplotlib.pyplot as plt   
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import learning_curve
import numpy as np
from sklearn.utils import shuffle

class test(object):

	def stratifiedFolds(self, ArrIn, ArrOut, K):

		TrainingIndexData = []
		TestIndexData = []
		TrainingInData = []
		TestInData = []
		TrainingOutData = []
		TestOutData = []

		random.shuffle(ArrIn) #Shuffles all values in array
		length = (math.floor(len(ArrIn)/K))*(K-1) #calculates size of training data
		remainder = len(ArrIn) % K #checks for remainder
		if remainder > 0:
			length += math.floor(remainder/2) #add half the remainder to training data
			if remainder % 2 != 0: #if remainder is an odd value
				length += 1 #add an extra value to training data
		#training data contains everything up to length
		TrainingInData += ArrIn[:length] 
		TrainingOutData += ArrOut[:length]
		#Test data contains everything after length
		TestInData += ArrIn[length:]
		TestOutData += ArrOut[length:]

		return TrainingInData, TestInData, TrainingOutData, TestOutData
	
	def rocCurve(self, ArrOutTest, probsArr, className):
		fpr, tpr, thresholds = metrics.roc_curve(ArrOutTest, probsArr, pos_label=1)
		roc_auc = metrics.auc(fpr, tpr) #Calculate area under the curv
		minDist = (2.0) ** 0.5 
		minX = 0.0
		minY = 0.0
		for counter in range(0, len(fpr)):  
			dist = ((fpr[counter] - 0)**2 + (tpr[counter] - 1)**2)**0.5  
			if dist < minDist:  
				minDist = dist  
				minX = fpr[counter]  
				minY = tpr[counter]  

		plt.figure(8) #figure definitin
		plt.xlabel('False Positive Rate') #xlabel
		plt.ylabel('True Positive Rate') #ylabel
		plt.title('ROC Curve')#classifier + ' ROC Curve') #title
		#plots fpr (x) against tpr (y). Adds details to the legend about AUC and min distance to (0,1)
		plt.plot(fpr, tpr, label= className + ' AUC = %0.2f\nMin dist to (0,1): %0.2f \nat point: (%0.2f,%0.2f)' % (roc_auc, minDist, minX, minY))  
		plt.legend(loc="lower right") #adds legend
		#plt.show() #displays figure
	
	@staticmethod
	def confusion_matrix(act, pred):
		return confusion_matrix(act, pred)

	def plot_learning_curve(self, estimator, title, X, y):
		"""
		Taken from scikit learn https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html
		"""
		plt.figure()
		plt.title(title)
		plt.xlabel("Training examples")
		plt.ylabel("Score")
		"""
		indices = list(range(len(y)))
		random.shuffle(indices)
		XShuff = np.empty(X.shape)
		yShuff = []
		for index in indices:
			nIndex = np.array([index])
			print(nIndex)
			XShuff = X[nIndex]
			print(XShuff)
			#XShuff = np.append(X[nIndex])
			yShuff.append(y[index])
		hi = hiThere
		"""
		X, y = shuffle(X, y)
		train_sizes, train_scores, test_scores = learning_curve(
			estimator, X, y, cv=10)
		train_scores_mean = np.mean(train_scores, axis=1)
		train_scores_std = np.std(train_scores, axis=1)
		test_scores_mean = np.mean(test_scores, axis=1)
		test_scores_std = np.std(test_scores, axis=1)
		plt.grid()

		plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
							train_scores_mean + train_scores_std, alpha=0.1,
							color="r")
		plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
							test_scores_mean + test_scores_std, alpha=0.1, color="g")
		plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
					label="Training score")
		plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
					label="Cross-validation score")

		plt.legend(loc="best")
		return plt
		"""
		for i in range(len(ArrIn)):
			random.shuffle(ArrIn[i])
			length = (math.floor(len(ArrIn[i])/K))*2
			remainder = len(ArrIn[i]) % K

			if remainder > 0:
				length += math.floor(remainder/2)
				if remainder % 2 != 0:
					length += 1

			TrainingIndexData += ArrIn[i][:length]
			TestIndexData += ArrIn[i][length:]

		for elem in TrainingIndexData:

			TrainingInData.append(ArrIn[elem])
			TrainingOutData.append(ArrOut[elem])

		for elem in TestIndexData:
			TestInData.append(ArrIn[elem])
			TestOutData.append(ArrOut[elem])

		return TrainingInData, TestInData, TrainingOutData, TestOutData
		"""