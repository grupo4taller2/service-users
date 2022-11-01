from pymongo import mongo_client
import pymongo
import os

#mongodb+srv://fiuber:<password>@fiuber.gojhw5h.mongodb.net/?retryWrites=true&w=majority

#'mongodb://mongodb:27017/'
client = mongo_client.MongoClient(os.environ['MONGO_ATLAS'])


print('Connected to MongoDB...')

db = client["fastapi"]

driver_collection = db.driver_collection

passenger_collection = db.passenger_collection