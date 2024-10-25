from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse
#Connect to the mongo shell
class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""
    def __init__(self, username, password):

        self.username = username
        self.password = password
        

        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:31431/?authSource=AAC')
        self.database = self.client['AAC']  
        self.collection = self.database.animals
       
    def create(self, data):
        #Check if new animal exists, insert and return the animal name if it does
        if data is not None:
            result = self.collection.insert_one(data)
            return data.get("name") 
        #Raise exception and print error if the animal does not exist
        else:
            raise Exception("Nothing to save, because data parameter is empty")
#Method to query for an animal 
    def getAnimal(self, query):
        #Check if the animal exists and return result if it does
        if query is not None:
            cursor = self.collection.find(query, {'_id': 0}) 
            
            result = list(cursor) 
            
            if result:
                return result 
            else:
                return []  
        #Raise exception and print error if the animal does not exist
        else:
            raise Exception("Query is empty")
#Method to update animal info
            
    def updateAnimal(self, query, newVal):
        #Check if animal exists and that new values for that animal exist, raise exception and print error if either do not exist
        if not query:
            raise Exception("Parameters returned no records")
        elif not newVal:
            raise Exception("No new value to update")
        #If animal and values exist update the animal and return the updated information
        else:
            updateVal = self.database.animals.update_many(query, {"$set": newVal})
            return updateVal.modified_count
#Method to delete animal    
    def deleteAnimal(self, query):
        #Check if animal exists, raise exception and print error if it does not
        if not query:
            raise Exception("Parameters returned no records")
        #If animal(s) exists delete them and print number of animals deleted
        else:
            deleteEntry = self.database.animals.delete_many(query)
            return deleteEntry.deleted_count 