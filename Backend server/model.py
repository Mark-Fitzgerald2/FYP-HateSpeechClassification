from preprocessing import preprocessing
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pickle

class model(object):

    def __init__(self):	
        self.prePro = preprocessing()

    def main(self):
        hateSpeech = pd.read_csv('~/hateSpeech/HateSpeech.csv', names=['Tweet', 'Hate'])
        nonHate = pd.read_csv('~/hateSpeech/NonHatePhrases.csv', names=['Tweet', 'Hate'])
        hateSpeech.loc[hateSpeech["Hate"]=="Hate", "Hate"] = 1
        nonHate.loc[nonHate["Hate"]=="Not Hate", "Hate"] = 0
        hateSpeech_x = hateSpeech["Tweet"]
        hateSpeech_y = hateSpeech["Hate"]
        nonHate_x = nonHate["Tweet"]
        nonHate_y = nonHate["Hate"]
            
        self.train_X = nonHate_x.tolist() + hateSpeech_x.tolist()
        self.train_Y = nonHate_y.tolist() + hateSpeech_y.tolist()
        
        self.trainXVect = self.processTrain(self.train_X)
        
        self.classifier = MultinomialNB()
        self.classifier.fit(self.trainXVect, self.train_Y)
        self.modelPersist()
		
    def modelPersist(self):
        pickleOut = open("model.p", "wb")
        pickle.dump(self.classifier, pickleOut)
        pickleOut.close()
        
    def processTrain(self, tweets):
        return self.prePro.creatTFVector(tweets)

    def processTest(self, tweets):
        return self.prePro.transformTest(tweets)
        
    def transformText(self, tweets):
        return self.prePro.transformText(tweets)

if __name__ == '__main__':
	main()