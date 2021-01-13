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
col_645 = db["t_645"]  # Collect(Table)
col_655 = db["t_655"]  # Collect(Table)

# Filter 645

def main():
    objLatest = col_645.find_one()
    for x in objLatest:
        print(len(x))
        data = json.loads(x)
        print(data)

if __name__ == '__main__':
    main()