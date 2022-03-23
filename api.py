from flask import Flask , jsonify, request
import requests
import csv

allarticle=[]
likedarticle=[]
dislikedarticle=[]


with open('articles.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    print(reader)
    data = list(reader)
    allarticles=data[1:]
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        "data":,
        "status":"success"
    })

@app.route('/getarticle' )
def getarticles():
    return jsonify({
        "data":allarticles[0],
        "status":"success"
    })
@app.route('/getlikedarticla',methods=['POST'])
def getlikedarticles():
    articles=allarticles[0]
    allarticlea=allarticles[1:]
    likedarticlea.append(articles)
    return jsonify({
        "status":sucess
    })
@app.route('/getdislikedarticle',methods=['POST'])
def getdislikedarticles():
    articles=allarticles[0]
    allarticlea=allarticles[1:]
    dislikedarticles.append(articles)
    return jsonify({
        "status":sucess
    })    
   

if __name__ == '__main__':
    app.run(debug=True)



