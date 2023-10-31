from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)  
db = client['ResearchClark']
collection = db['basicCo']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/views/")
def index():
    data = list(collection.find({}))  
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

