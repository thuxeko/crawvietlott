from pymongo import MongoClient

from credentials import mongo_connect

client = MongoClient(mongo_connect)
db = client['data_vietlott']  # Database
col_645 = db["t_645"]  # Collect(Table)
col_655 = db["t_655"]  # Collect(Table)

#region Filter 645
# Delete value
# col_645.delete_many({})
# col_655.delete_many({})
#endregion

#region Insert
# with open('645.json') as json_file:
#     data = json.load(json_file)
#     col_645.insert_many(data)

# with open('655.json') as json_file:
#     data = json.load(json_file)
#     col_655.insert_many(data)
#endregion

def getLatest645():
  objLatest645 = col_645.find({},{ "_id": 0, "KyQuay": 1 }).sort('KyQuay',-1).skip(0).limit(1)
  return objLatest645[0]["KyQuay"]

def getLatest655():
  objLatest655 = col_655.find({},{ "_id": 0, "KyQuay": 1 }).sort('KyQuay',-1).skip(0).limit(1)
  return objLatest655[0]["KyQuay"]

def insert645(obj):
    obj645 = col_645.insert_one(obj)
    return obj645.inserted_id

def insert655(obj):
    obj655 = col_655.insert_one(obj)
    return obj655.inserted_id