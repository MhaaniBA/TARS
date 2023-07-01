
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Bank:
    def __init__(self,mdbusername=None,mdbpassword=None,mdbdatabase=None,mdbcollection=None):
        self.mdbusername = mdbusername
        self.mdbpassword = mdbpassword
        self.mdbdatabase = mdbdatabase
        self.mdbcollection = mdbcollection
    
    def connector(self):
        uri = "mongodb://localhost:27017/"
        # Create a new client and connect to the server
        client = MongoClient(uri)

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            db = client['tarsdb']
            collection = db['tarscoll']
            return db,collection,client
        except Exception as e:
            print(e)

    def sub_connector(self,collection):
        uri = "mongodb://localhost:27017/"
        # Create a new client and connect to the server
        client = MongoClient(uri)

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            db = client['tarsdb']
            collection = db[f'{collection}']
            return db,collection,client
        except Exception as e:
            print(e)

    # Package all annotations ready for shipment (mongodb)
    def containerize(self,nodes):
        jsonpeg = []
        for i in nodes:
            node = {
                "_id": i["id"],
                "created": i["created"][:10],
                "updated": i["updated"][:10],
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




