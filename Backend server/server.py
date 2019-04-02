from classifier import classifier
from flask import Flask, request
from flask_cors import CORS, cross_origin
from streamer import streamer
import time
import json
import numpy as np

app = Flask(__name__)
CORS(app, support_credentials=True)
print("Loading Classification Model")
model = classifier()

@app.route("/classifyText", methods=["POST"])
@cross_origin(origin='danu6.it.nuigalway.ie/mFitzgerald1/', headers=['Content- Type','Authorization'], support_credentials=True)
def classifyText():
	data = request.get_json()
	prediction, probability = model.classify([data["text"]])
	if prediction == 1:
	    pred = "Yes"
	    prob = str(round(probability[0][1]*100,2)) + "%"
	else:
	    pred = "No"
	    prob = str(round(100-probability[0][1]*100,2)) + "%"
    

	maxWords = 5
	wordArray = data["text"].split()
	wordArray = list(map(str.lower, wordArray))
	wordArray = list(dict.fromkeys(wordArray))
	data = []
	labels = []
	for word in wordArray:
		if len(data) < maxWords:
			prediction, probability = model.classify([word])
			if prediction == 1:
				labels.append(word)
				data.append(round(probability[0][1] * 100,2))
		else:
			prediction, probability = model.classify([word])
			if prediction == 1:
				oldData = data[:]
				oldLabels = labels[:]
				data.sort() 
				j = 0
				indices = [data.index(d) for d in oldData]
				for i in indices:
					labels[i] = oldLabels[j]
					j += 1
				numpyData = np.array(data)
				numpyCheck = numpyData < probability[0][1]
				try:
					index = numpyCheck.tolist().index(True)
					labels[index] = word
					data[index] = round(probability[0][1] * 100,2)
				except Exception as e:
					print(e) 
	output = {
		"pred": pred,
		"prob": prob,
		"data": data,
		"labels": labels
	}
	return json.dumps(output), 200
 
@app.route("/classifyTwitterAcc", methods=["POST"])   
def classifyTwitterAcc():
	data = request.get_json()
	tweets = streamer(data["twitterId"], data["numTweets"]).readUserAccount()
	predictions, probability = model.classify(tweets)
	hate = 0 
	nonHate = 0
	labels = ["<50%", "50-60%", "60-70%","70-80%", ">80%"]
	data = [0,0,0,0,0]
	for i in range(len(predictions)):	    
	    if predictions[i] == 1:
	        hate += 1
	        if probability[i][1]<0.60:
	            temp = data[1]
	            data[1] = temp + 1
	        elif probability[i][1]<0.70:
	            temp = data[2]
	            data[2] = temp + 1
	        elif probability[i][1]<0.80:
	            temp = data[3]
	            data[3] = temp + 1
	        else:
	            temp = data[4]
	            data[4] = temp + 1
	    else:
	        nonHate += 1
	        temp = data[0]
	        data[0] = temp + 1	
	percent = (hate / (hate + nonHate)) * 100
	out = ""
	if percent > 25:
	    out = "Yes"
	else:
	    out = "No"

	output = {
	    "pred": out,
            "prob": str(percent) + "%",
            "labels": labels,
            "data": data
	}
	return json.dumps(output), 200
    
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)

