from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.stem.snowball import SnowballStemmer

cv = TfidfVectorizer(min_df=1, stop_words=None, use_idf=False)
x_traincv = cv.fit_transform(["Hi how are you, how are you doing?", "Hey what's up?", "Hey cool tutorial"])
print(cv.get_feature_names())
print(x_traincv.toarray())

cv1 = TfidfVectorizer(min_df=1, stop_words=None, use_idf=True)
x_traincv1 = cv1.fit_transform(["Hi how are you, how are you doing?", "Hey what's up?", "Hey cool tutorial"])
print(cv1.get_feature_names())
print(x_traincv1.toarray())
sbStemmer = SnowballStemmer('english')
print(sbStemmer.stem('fucking'))