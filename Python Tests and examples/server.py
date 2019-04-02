from classifier import classifier
from flask import Flask, request
from flask_cors import CORS
from streamer import streamer
import time
import json

app = Flask(__name__)
CORS(app)
print("Loading Classification Model")
model = classifier()

@app.route("/classifyText", methods=["POST"])

def classifyText():
    data = request.get_json()
    prediction, probability = model.classify([data["text"]])
    if prediction == 1:
        pred = "Yes"
        prob = str(round(probability[0][1]*100,2)) + "%"
    else:
        pred = "No"
        prob = str(round(100-probability[0][1]*100,2)) + "%"
    #print(prediction)
    #print(probability) 
    output = {
        "pred": pred,
        "prob": prob
    }
    return json.dumps(output), 200
 
@app.route("/classifyTwitterAcc", methods=["POST"])   

def classifyTwitterAcc():
    data = request.get_json()
    t1 = time.time()
    tweets = streamer(data["twitterId"], data["numTweets"]).readUserAccount()
    t2 = time.time()
    #print("Twitter API time taken: {:.2f}".format(t2 - t1))
    predictions, probability = model.classify(tweets)
    #print(predictions)
    hate = 0 
    nonHate = 0
    for pred in predictions:
        if pred == 1:
            hate += 1
        else:
            nonHate += 1
    percent = (hate / (hate + nonHate)) * 100
    out = ""
    if percent > 25:
        out = "Yes"
    else:
        out = "No"

    output = {
        "pred": out,
        "prob": str(percent) + "%"
    }
    #print("This account makes use of hate speech: ", out)
    #print("Number of tweets which contained hate speech: ", percent)
    #string = "This account makes use of hate speech: " +  out
    return json.dumps(output), 200
    
    
if __name__ == "__main__":
    app.run()

