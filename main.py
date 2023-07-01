import requests
import os
import pandas as pd
import json
import plotly
import plotly.express as px
import pandas
from datetime import datetime

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

        return render_template('index.html',Keys=Keys)

    elif request.method=="POST":        
        Keys.HUGGINGFACE_API_KEY = request.form.get('hugg')
        Keys.HYPOTHESIS_API_KEY = request.form.get('hyp')
        Keys.HYPOTHESIS_USERNAME = request.form.get('hypus')


    
        with open(f"{os.getcwd()}/register.txt",'a') as register:
            register.write(Keys.HUGGINGFACE_API_KEY+"\n")
            register.write(Keys.HYPOTHESIS_API_KEY+"\n")
            register.write(Keys.HYPOTHESIS_USERNAME+"\n")


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
    a = bank.containerize(Keys.node_dispatcher())
    d = {}
    for i in a:
        if i['created'][:10] in d:
            d[i['created'][:10]] +=1
        else:
            d[i['created'][:10]] = 1
    
    date_format = '%Y-%m-%d'
    a  = pd.DataFrame.from_dict(d, orient='index', columns=['Value'])
    a.index = pd.to_datetime(a.index)
    fig = px.bar(a,labels={"value":"Annotaions","index":"Timeline"},barmode='group')
    graphJSON = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    
    db1,collection1,client1 = bank.sub_connector("stats")
    df = pd.DataFrame(list(collection1.find({})))
    df = pd.DataFrame.transpose(df)

    print(list(df.columns.values))
    
    print(df.count())

    
    return render_template('dashboard.html',Keys=Keys,graphJSON=graphJSON)


@app.route("/nodes")
def nodes():
    db,collection,client = bank.connector()
    jsonpeg = bank.containerize(Keys.node_dispatcher())
    bank.ship(collection,jsonpeg[:10])
    recieve = list(bank.recieve(collection))
    # print(recieve)
    return render_template('nodes.html',Keys=Keys,bank=bank,recieve=recieve)

@app.route("/tars",methods=['GET','POST'])
def tars():
    db,collection,client = bank.connector()
    jsonpeg = bank.containerize(Keys.node_dispatcher())
    question,answer = Keys.quiz_generator(jsonpeg)

    if request.method == "POST":
        d = {}
        input1 = request.form.get("input1")
        input2 = request.form.get("input2")
        points = Keys.quiz_assessor(input1,input2,answer)
        # print(points)
        # print(type(points))
        d[str(datetime.now())[:10]]=points

        db1,collection1,client1 = bank.sub_connector("stats")
        collection1.insert_one(d)


        return render_template('dashboard.html',question=question,answer=answer,Keys=Keys)

    return render_template('tars.html',Keys=Keys,question=question,answer=answer)
