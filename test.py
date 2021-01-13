import json
from pymongo import MongoClient

import logging

from credentials import mongo_connect

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

client = MongoClient(mongo_connect)
db = client['data_vietlott']  # Database
# col_645 = db["t_645"]  # Collect(Table)
col_655 = db["t_655"]  # Collect(Table)

def main():
    with open('data655.json') as json_file:
        data = json.load(json_file)
        col_655.insert_many(data)
        print("Insert thanh cong")

if __name__ == '__main__':
    main()