from pymongo import mongo_client
import os


client = mongo_client.MongoClient(os.environ['MONGO_ATLAS'])


print('Connected to MongoDB...')

db = client["fastapi"]

driver_collection = db.driver_collection

passenger_collection = db.passenger_collection
