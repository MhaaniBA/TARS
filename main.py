import requests

from package.hub import Hub
from package.bank import Bank
from flask import Flask, render_template,request


## Flask initial config 
app = Flask(__name__)

# map initialization
Keys = Hub()
bank = Bank()

## Route Setup
@app.route("/")
def index():
    return render_template('index.html',Keys=Keys)


@app.route("/save",methods=['GET','POST'])
def save():
    if request.method=="POST":
        Keys.HUGGINGFACE_API_KEY = request.form.get('hugg')
        Keys.HYPOTHESIS_API_KEY = request.form.get('hyp')
        Keys.HYPOTHESIS_USERNAME = request.form.get('hypus')
        bank.mdbusername = request.form.get('mdbus')
        bank.mdbpassword = request.form.get('mdbps')
        bank.mdbdatabase = request.form.get('mdbnm')
        bank.mdbcollection = request.form.get('mdbcoll')
        return render_template('index.html',Keys=Keys)
    else:
        return render_template('save.html',Keys=Keys)

@app.route("/forget")
def forget():
    Keys.HUGGINGFACE_API_KEY = None
    Keys.HYPOTHESIS_API_KEY = None
    return render_template('index.html',Keys=Keys)


@app.route("/dashboard")
def dashboard():
    
    return render_template('dashboard.html',Keys=Keys)


@app.route("/nodes")
def nodes():
    db,collection,client = bank.connector()
    jsonpeg = bank.containerize(Keys.node_dispatcher())
    bank.ship(collection,jsonpeg[:5])
    recieve = list(bank.recieve(collection))
    # print(recieve)
    return render_template('nodes.html',Keys=Keys,bank=bank,recieve=recieve)

@app.route("/tars")
def tars():
    return render_template('tars.html',Keys=Keys)