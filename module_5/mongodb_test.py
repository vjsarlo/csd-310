from pymongo import MongoClient

url = "mongodb+srv://admin:admin@sarlo-assignment4-2.5vuly.mongodb.net/pytech"

client = MongoClient(url, ssl=True,ssl_cert_reqs='CERT_NONE')

db = client.pytech

print(db.list_collection_names())