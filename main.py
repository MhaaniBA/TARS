from flask import Flask, render_template,request
from package.hub import Hub
import requests


## Flask initial config 
app = Flask(__name__)


Keys = Hub()
## Route Setup
@app.route("/")
def index():
    return render_template('index.html',Keys=Keys)


@app.route("/save",methods=['GET','POST'])
def save():
    if request.method=="POST":
        Keys.HUGGINGFACE_API_KEY = request.form.get('hugg')
        Keys.HYPOTHESIS_API_KEY = request.form.get('hyp')
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
    Nodes = Keys.node_dispatcher()
    return render_template('nodes.html',Keys=Keys,Nodes=Nodes)

@app.route("/tars")
def tars():
    return render_template('tars.html',Keys=Keys)