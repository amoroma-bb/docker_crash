from pymongo import MongoClient
from pprint import pp, pprint

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin

col = db.links
col.insert_one({"link": "stashchuk.com"})
links = col.find({})
for link in links:
    pprint(link)