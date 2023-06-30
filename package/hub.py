import requests
import random
class Hub:
  def __init__(self,HYPOTHESIS_API_KEY=None,HUGGINGFACE_API_KEY=None,HYPOTHESIS_USERNAME="thlurte"):
    self.HYPOTHESIS_USERNAME = HYPOTHESIS_USERNAME
    self.HYPOTHESIS_API_KEY = HYPOTHESIS_API_KEY
    self.HUGGINGFACE_API_KEY = HUGGINGFACE_API_KEY
    
  def node_dispatcher(self):
    """
    Function -> returns all nodes from hypothsis.is
    """
    headers = { "Authorization": f"Bearer {self.HYPOTHESIS_API_KEY}" }
    para    = { "limit":50,"user": f"acct:{self.HYPOTHESIS_USERNAME}@hypothes.is" }
    api_url = "https://hypothes.is/api/search"
    return requests.get(api_url,headers=headers,params=para).json()['rows']

  def quiz_generator(self,jsonpeg):
    """
    Function -> returns a question based on the input
    """
    API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"
    headers = {"Authorization": "Bearer {self.HUGGINGFACE_API_KEY}"}
    peg = random.choice(jsonpeg)
    shapedpeg = f"{peg['annotation']}{peg['highlight']}"
    def query(payload):
      response = requests.post(API_URL, headers=headers, json=payload)
      return response.json()

    return query({"inputs": "context: {shapedpeg}"})

  def quiz_assessor(self,input):
    pass


