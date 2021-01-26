from selenium import webdriver
from time import sleep
import json
import os
from pymongo import MongoClient
import logging

from credentials import mongo_connect

chromePath = "D:/chromedriver/chromedriver.exe"
dv = webdriver.Chrome(executable_path=chromePath)

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)

# client = MongoClient(mongo_connect)
# db = client['data_vietlott']  # Database
# col_645 = db["t_645"]  # Collect(Table)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")

# dv = webdriver.Chrome(executable_path=os.environ.get(
#             "CHROMEDRIVER_PATH"), chrome_options=chrome_options)

lstOut = []

dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645")

# Wait load page
for x in range(689):
    if x == 0:
        objBall = dv.find_elements_by_xpath("//*[contains(@class, 'bong_tron')]")
        objText = dv.find_elements_by_xpath("//div[@class='chitietketqua_title']/h5/b")

        objTic = {
            "KyQuay": int(objText[0].text.replace("#", "")),
            "NgayQuay": objText[1].text,
            "Number_1": int(objBall[0]),
            "Number_2": int(objBall[1]),
            "Number_3": int(objBall[2]),
            "Number_4": int(objBall[3]),
            "Number_5": int(objBall[4]),
            "Number_6": int(objBall[5])
        }
        print("Ky: " + str(objTic["KyQuay"]))
        lstOut.append(objTic)
    else:
        prButton = dv.find_element_by_xpath(
            "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[2]/a[1]"
        )
        prButton.click()
        sleep(5)

        objBallN = dv.find_elements_by_xpath("//*[contains(@class, 'bong_tron')]")
        objTextN = dv.find_elements_by_xpath("//div[@class='chitietketqua_title']/h5/b")

        objTic = {
            "KyQuay": int(objTextN[0].text.replace("#", "")),
            "NgayQuay": objTextN[1].text,
            "Number_1": int(objBallN[0]),
            "Number_2": int(objBallN[1]),
            "Number_3": int(objBallN[2]),
            "Number_4": int(objBallN[3]),
            "Number_5": int(objBallN[4]),
            "Number_6": int(objBallN[5])
        }
        print("Ky: " + str(objTic["KyQuay"]))
        lstOut.append(objTic)

with open('645.json', 'w') as outfile:
    json.dump(lstOut, outfile)