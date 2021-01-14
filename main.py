import schedule
import time
import mongoQuery
import getVietlott
from datetime import date,datetime

def get655():
  obj655 = getVietlott.get655Data()
  print("Ky: " + str(obj655["KyQuay"]))
  print("Insert to Mongo")
  id_mongo = mongoQuery.insert655(obj655)

  print("Insert thanh cong: " + str(id_mongo))

def get645():
  obj645 = getVietlott.get645Data()
  print("Ky: " + str(obj645["KyQuay"]))
  print("Insert to Mongo")
  id_mongo = mongoQuery.insert645(obj645)

  print("Insert thanh cong: " + str(id_mongo))

# Get 645
schedule.every().wednesday.at('11:00').do(get645)
schedule.every().friday.at('11:00').do(get645)
schedule.every().sunday.at('11:00').do(get645)

# Get 655
schedule.every().tuesday.at('11:00').do(get655)
schedule.every().thursday.at('11:00').do(get655)
schedule.every().saturday.at('11:00').do(get655)

while True:
  schedule.run_pending()
  time.sleep(1)