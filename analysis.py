from pymongo import MongoClient
from credentials import mongo_connect

client = MongoClient(mongo_connect)
db = client["data_vietlott"]  # Database
col_645 = db["t_645"]  # Collect(Table)
col_655 = db["t_655"]  # Collect(Table)

# oob2 = col_645.aggregate([{
#     "$project": {
#         "Number_1": 1,
#         "Number_2": 1,
#         "Number_3": 1,
#         "Number_4": 1,
#         "Number_5": 1,
#         "Number_6": 1
#     }
# }, {
#     "$group": {
#         "_id": {
#             "number1": "$Number_1"
#         },
#         "count": {
#             "$sum": 1
#         },
#     }
# }])

# 645
oob2 = col_645.aggregate(
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
        {"$sort" : { "_id.numOut" : 1 }}
    ]
)

for x in oob2:
    print(x)