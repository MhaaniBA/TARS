import requests
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

  def key_register(self)