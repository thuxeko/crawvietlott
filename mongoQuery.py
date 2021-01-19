from pymongo import MongoClient
import json
from credentials import mongo_connect

client = MongoClient(mongo_connect)
db = client["data_vietlott"]  # Database
col_645 = db["t_645"]  # Collect(Table)
col_655 = db["t_655"]  # Collect(Table)

# region Filter 645
# Delete value
# col_645.delete_many({})
# col_655.delete_many({})
# endregion

# region Insert
# with open('645.json') as json_file:
#     data = json.load(json_file)
#     col_645.insert_many(data)

# with open('655.json') as json_file:
#     data = json.load(json_file)
#     col_655.insert_many(data)
# endregion


def getLatest645():
    objLatest645 = (
        col_645.find({}, {"_id": 0, "KyQuay": 1}).sort("KyQuay", -1).skip(0).limit(1)
    )
    return objLatest645[0]["KyQuay"]


def getLatest655():
    objLatest655 = (
        col_655.find({}, {"_id": 0, "KyQuay": 1}).sort("KyQuay", -1).skip(0).limit(1)
    )
    return objLatest655[0]["KyQuay"]


def insert645(obj):
    obj645 = col_645.insert_one(obj)
    return obj645.inserted_id


def insert655(obj):
    obj655 = col_655.insert_one(obj)
    return obj655.inserted_id


# Cau lenh Remove Duplicate(Dung cho moi truong hop)
def removeDuplicate():
    duplicates = []
    oob2 = col_655.aggregate(
        [
            {"$match": {"name": {"$ne": ""}}},
            {
                "$group": {
                    "_id": {"name": "$KyQuay"},
                    "dups": {"$addToSet": "$_id"},
                    "count": {"$sum": 1},
                }
            },
            {"$match": {"count": {"$gt": 1}}},
        ]
    )

    for x in oob2:
        duplicates.append(x["dups"][1])
    col_655.delete_many({"_id": {"$in": duplicates}})


def analysis645():
    lst645 = []
    obj = col_645.aggregate(
        [
            {
                "$facet": {
                    "Number1": [{"$project": {"_id": 0, "num": "$Number_1"}}],
                    "Number2": [{"$project": {"_id": 0, "num": "$Number_2"}}],
                    "Number3": [{"$project": {"_id": 0, "num": "$Number_3"}}],
                    "Number4": [{"$project": {"_id": 0, "num": "$Number_4"}}],
                    "Number5": [{"$project": {"_id": 0, "num": "$Number_5"}}],
                    "Number6": [{"$project": {"_id": 0, "num": "$Number_6"}}],
                }
            },
            {
                "$project": {
                    "data": {
                        "$concatArrays": [
                            "$Number1.num",
                            "$Number2.num",
                            "$Number3.num",
                            "$Number4.num",
                            "$Number5.num",
                            "$Number6.num",
                        ]
                    }
                }
            },
            {"$unwind": "$data"},
            {"$group": {"_id": {"numOut": "$data"}, "count": {"$sum": 1}}},
            {"$sort": {"_id.numOut": 1}},
        ]
    )
    for x in obj:
        lst645.append({"Number": x["_id"]["numOut"], "Count": x["count"]})

    return json.dumps(lst645)


def analysis655():
    lst655 = []
    obj = col_655.aggregate(
        [
            {
                "$facet": {
                    "Number1": [{"$project": {"_id": 0, "num": "$Number_1"}}],
                    "Number2": [{"$project": {"_id": 0, "num": "$Number_2"}}],
                    "Number3": [{"$project": {"_id": 0, "num": "$Number_3"}}],
                    "Number4": [{"$project": {"_id": 0, "num": "$Number_4"}}],
                    "Number5": [{"$project": {"_id": 0, "num": "$Number_5"}}],
                    "Number6": [{"$project": {"_id": 0, "num": "$Number_6"}}],
                    "Number7": [{"$project": {"_id": 0, "num": "$Number_Bonus"}}],
                }
            },
            {
                "$project": {
                    "data": {
                        "$concatArrays": [
                            "$Number1.num",
                            "$Number2.num",
                            "$Number3.num",
                            "$Number4.num",
                            "$Number5.num",
                            "$Number6.num",
                            "$Number7.num",
                        ]
                    }
                }
            },
            {"$unwind": "$data"},
            {"$group": {"_id": {"numOut": "$data"}, "count": {"$sum": 1}}},
            {"$sort": {"_id.numOut": 1}},
        ]
    )
    for x in obj:
        lst655.append({"Number": x["_id"]["numOut"], "Count": x["count"]})

    return json.dumps(lst655)


def findWithDate(typeS, fromdate, todate):
    if typeS == 645:
        objLatest645 = col_645.aggregate(
            [
                {
                    "$addFields": {
                        "date_convert": {
                            "$dateFromString": {
                                "dateString": "$NgayQuay",
                                "format": "%d/%m/%Y",
                            }
                        }
                    }
                },
                {"$match": {"date_convert": {"$gte": fromdate, "$lt": todate}}},
                {"$sort": {"KyQuay": -1}},
            ]
        )

        return objLatest645
    else:
        objLatest655 = col_645.aggregate(
            [
                {
                    "$addFields": {
                        "date_convert": {
                            "$dateFromString": {
                                "dateString": "$NgayQuay",
                                "format": "%d/%m/%Y",
                            }
                        }
                    }
                },
                {"$match": {"date_convert": {"$gte": fromdate, "$lt": todate}}},
                {"$sort": {"KyQuay": -1}},
            ]
        )

        return objLatest655


def findWithDayOfWeek(typeS, lstDay):
    if typeS == 645:
        objLatest645 = col_645.aggregate(
            [
                {
                    "$addFields": {
                        "dayofweek": {
                            "$dayOfWeek": {
                                "$dateFromString": {
                                    "dateString": "$NgayQuay",
                                    "format": "%d/%m/%Y",
                                }
                            }
                        }
                    }
                },
                {"$match": {"dayofweek": {"$in": lstDay}}},
            ]
        )

        return objLatest645
    else:
        objLatest655 = col_655.aggregate(
            [
                {
                    "$addFields": {
                        "dayofweek": {
                            "$dayOfWeek": {
                                "$dateFromString": {
                                    "dateString": "$NgayQuay",
                                    "format": "%d/%m/%Y",
                                }
                            }
                        }
                    }
                },
                {"$match": {"dayofweek": {"$in": lstDay}}},
            ]
        )
        return objLatest655