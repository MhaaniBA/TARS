
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Bank:
    def __init__(self,mdbusername=None,mdbpassword=None,mdbdatabase=None,mdbcollection=None):
        self.mdbusername = mdbusername
        self.mdbpassword = mdbpassword
        self.mdbdatabase = mdbdatabase
        self.mdbcollection = mdbcollection
    
    def connector(self):
        uri = f"mongodb+srv://{self.mdbusername}:{self.mdbpassword}@cluster0.ngwn7xx.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            db = client[f'{self.mdbdatabase}']
            collection = db[f'{self.mdbcollection}']
            return db,collection,client
        except Exception as e:
            print(e)

    def containerize(self,nodes):
        jsonpeg = []
        for i in nodes:
            node = {
                "_id": i["id"],
                "created": i["created"],
                "updated": i["updated"],
                "url": i["uri"],
                "annotation": i["text"],
                "tags": i["tags"],
                "highlight": i['target'][0]['selector'][1]['exact'] if len(i['target'][0]['selector']) == 2 else i['target'][0]['selector'][2]['exact'],  
                "title": i['document']['title'][0] if len(i['document'])!= 0 else ""
            }
            jsonpeg.append(node)
        return jsonpeg

    def ship(self,collection,jsonpeg):
        for peg in jsonpeg:
            if collection.find_one(peg)==None:
                collection.insert_one(peg)
            else:
                pass

    def disconnector(self,client):
        client.close()

    def recieve(self,collection):
        return collection.find()




