import requests
import os

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
    if os.path.exists("register.txt"):
        with open(f"{os.getcwd()}/register.txt","r") as register:
            lines = register.readlines()
            
        line_variables = []

        for line in lines:
            line_variables.append(line.strip())

        Keys.HUGGINGFACE_API_KEY = line_variables[0]
        Keys.HYPOTHESIS_API_KEY = line_variables[1]
        Keys.HYPOTHESIS_USERNAME = line_variables[2]
        bank.mdbusername = line_variables[3]
        bank.mdbpassword = line_variables[4]
        bank.mdbdatabase = line_variables[5]
        bank.mdbcollection = line_variables[6]
        return render_template('index.html',Keys=Keys)

    elif request.method=="POST":        
        Keys.HUGGINGFACE_API_KEY = request.form.get('hugg')
        Keys.HYPOTHESIS_API_KEY = request.form.get('hyp')
        Keys.HYPOTHESIS_USERNAME = request.form.get('hypus')
        bank.mdbusername = request.form.get('mdbus')
        bank.mdbpassword = request.form.get('mdbps')
        bank.mdbdatabase = request.form.get('mdbnm')
        bank.mdbcollection = request.form.get('mdbcoll')

    
        with open(f"{os.getcwd()}/register.txt",'a') as register:
            register.write(Keys.HUGGINGFACE_API_KEY+"\n")
            register.write(Keys.HYPOTHESIS_API_KEY+"\n")
            register.write(Keys.HYPOTHESIS_USERNAME+"\n")
            register.write(bank.mdbusername+"\n")
            register.write(bank.mdbpassword+"\n")
            register.write(bank.mdbdatabase+"\n")
            register.write(bank.mdbcollection+"\n")

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