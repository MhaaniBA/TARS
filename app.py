from flask import Flask, render_template,request

app = Flask(__name__)

class API_KEYS:
    def __init__(self,HYPOTHESIS_KEY=None,HUGGING_FACE_KEY=None):
        self.HYPOTHESIS_KEY = HYPOTHESIS_KEY
        self.HUGGING_FACE_KEY = HUGGING_FACE_KEY 

Keys = API_KEYS()

@app.route("/")
def index():
    return render_template('index.html',Keys=Keys)


@app.route("/save",methods=['GET','POST'])
def save():
    if request.method == "POST":
        Keys.HUGGING_FACE_KEY = request.form.get('hugg')
        Keys.HYPOTHESIS_KEY = request.form.get('hyp')
        return render_template('index.html',Keys=Keys)
    else:
        return render_template('save.html',Keys=Keys)

@app.route("/forget")
def forget():
    Keys.HUGGING_FACE_KEY = None
    Keys.HYPOTHESIS_KEY = None
    return render_template('index.html',Keys=Keys)


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html',Keys=Keys)


@app.route("/nodes")
def nodes():
    return render_template('nodes.html',Keys=Keys)

@app.route("/tars")
def tars():
    return render_template('tars.html',Keys=Keys)