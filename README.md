<p align="center">
  <b> ~ TARS ~ </b>
</p>
<div align="center">
    <p></p>
    <a href="https://github.com/thlurte/dots/stargazers">
        <img src="https://img.shields.io/github/stars/thlurte/dots?color=%23BB9AF7&labelColor=%231A1B26&style=for-the-badge">
    </a>
        <img src="https://img.shields.io/github/forks/thlurte/dots?color=%237AA2F7&labelColor=%231A1B26&style=for-the-badge">
    </a>
</div>
<div>
<img src="assets/2023-07-01_22-47.png" align="center">
 </div>


<br/>
<p align="center"> a personal learning space with flask and hypothesis.io  </p>
<br/>

## Features

### Dashboard
- plotly for visualizing the data related to the nodes captured and questions answered.
<img src="assets/2023-07-01_22-48.png" align="center">

### Nodes
- annotations(nodes) captured from Hypothesis.io are stored in MongoDB local database
<img src="assets/2023-07-01_22-48_1.png" align="center">

### Assessment
- HuggingFace api's to generate questions and assess answers based on the node.
<img src="assets/2023-07-01_22-49.png" align="center">


## Installation

### Dependancies

```bash
pip install virtualenv
```

- [MongoDB Community Edition](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
- [virtualenv](https://pypi.org/project/virtualenv/)

### Process

Clone the repo into a prefered directory.
```bash
git clone git@github.com:Thlurte/TARS.git
```
cd into the repo
```
cd TARS/
```
activate  virtual environment
```
source venv/bin/activate
```
run the application
```
flask --app main run
```
## Credits
- [mrm8488/t5-base-finetuned-question-generation-ap](https://huggingface.co/mrm8488/t5-base-finetuned-question-generation-ap)
- [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)





