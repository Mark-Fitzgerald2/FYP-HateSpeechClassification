import numpy as np

class rocCurveGen(object):
	
	def main(self):
		tpRates = []
		fpRates = []

		TPRateArr = []
		FPRateArr = []

		for Threshold in np.linspace(0,1,1000):

			predictedClass = []
			for prob in probsArr:
				if prob >= Threshold:
					#Positive
					predictedClass.append('positive')
					#print('Positive')
				else:
					#Negative
					predictedClass.append('negative')
					#print('Negative')
			print(predictedClass)
			TN = TP = FP = FN = 0
			for count in range(0, len(ArrOutTest[i])):
				if predictedClass[count] == ArrOutTest[i][count]:
					if predictedClass[count] == 'positive':
						TP += 1
					elif predictedClass[count] == 'negative':
						TN += 1
				else: 
					if predictedClass[count] == 'positive':
						FP += 1
					elif predictedClass[count] == 'negative':
						FN += 1
			print('True Positive: ', TP)
			print('False Positive: ', FP)
			print('True Negative: ', TN)
			print('False Negative: ', FN)
			TPRate = TP/(TP+FN)
			FPRate = FP/(FP+TN)
			TPRateArr.append(TPRate)
			FPRateArr.append(FPRate)
		fpRates.append(FPRateArr)
		tpRates.append(TPRateArr)

		return fpRates, tpRates