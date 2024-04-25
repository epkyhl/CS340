from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30302
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Method to create a record in the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True  # Returns True for confirmation of successful creation
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False  # Returns False for an empty dataset or other error in creation

# Method to read records in the database
    def read(self, data):
    	if data is not None:
    	    query = list(self.database.animals.find(data))
    	    return query  # Returns the record if successfully found
    	else:
    	    raise Exception("Nothing to read, because data parameter is empty")
    	    return []  # Returns an empty list if record not found or other error occurs

# Method to update records in the database
    def update(self, queryData, updatedData):
    	if queryData is not None:
    	    if updatedData is None:
    	    # Will replace value with empty string if no value is provided
    	        updatedData = ""  
    	    queryUpdate = self.database.animals.update(queryData, {"$set":updatedData})
    	    return queryUpdate  # Returns number of objects modified, if any
    	else:
    	    raise Exception("Nothing to update, because the data parameter is empty")
    	    return []  # Returns empty list if the update is not attempted

# Method to delete records in the database
    def delete(self, data):
        if data is not None:
            deletedQueries = self.database.animals.delete_many(data)
            return deletedQueries  # Returns number of deleted queries, if any
        else:
            raise Exception("Nothing to delete, because the data parameter is empty")
            return[]  # Returns empty list if delete is not attempted
