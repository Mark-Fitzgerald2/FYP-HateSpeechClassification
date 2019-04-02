import pickle
from preprocessing import preprocessing
from model import model

class classifier(object):
    
    def __init__(self):	
        self.prePro = preprocessing()
        self.model = model()
        try:
            pickleIn = open("model.p", "rb")
            self.classifier = pickle.load(pickleIn)
        except (OSError, IOError) as e:
            self.model.main()
            pickleIn = open("model.p", "rb")
            self.classifier = pickle.load(pickleIn)
            
    def classify(self, tweet):
        self.tweetVect = self.model.transformText(tweet)
        self.pred = self.classifier.predict(self.tweetVect)
        self.prob = self.classifier.predict_proba(self.tweetVect)
        return self.pred, self.prob
        