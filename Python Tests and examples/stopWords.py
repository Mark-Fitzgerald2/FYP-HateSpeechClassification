from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
s = '... some string with punctuation ...'
#s = s.translate(None, string.punctuation) Python 2
s = s.translate(str.maketrans('','',string.punctuation)) #Python 3
 
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []
stopWordsArr = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
    else:
    	stopWordsArr.append(w)
 
print(wordsFiltered)

print("*****stop words*****")
print(stopWordsArr)

print("*****No punctuation*****")
print(s)