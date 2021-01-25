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

objBall = dv.find_elements_by_xpath("//*[contains(@class, 'bong_tron')]")
objBall = dv.find_elements_by_xpath("//span[contains(@class, 'bong_tron')]")

for x in objBall:
    print(x.text)
# Wait load page
# for x in range(689):
#     if x == 0:
#         objTic = {
#             "KyQuay": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[1]"
#             ).text.replace("#", "")),
#             "NgayQuay": dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[2]"
#             ).text,
#             "Number_1": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
#             ).text.replace("#", "")),
#             "Number_2": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
#             ).text.replace("#", "")),
#             "Number_3": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
#             ).text.replace("#", "")),
#             "Number_4": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
#             ).text.replace("#", "")),
#             "Number_5": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
#             ).text.replace("#", "")),
#             "Number_6": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
#             ).text.replace("#", ""))
#         }
#         print("Ky: " + str(objTic["KyQuay"]))
#         lstOut.append(objTic)
#     else:
#         prButton = dv.find_element_by_xpath(
#             "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[2]/a[1]"
#         )
#         prButton.click()
#         sleep(5)
#         objTic = {
#             "KyQuay": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[1]"
#             ).text.replace("#", "")),
#             "NgayQuay": dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[2]"
#             ).text,
#             "Number_1": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
#             ).text.replace("#", "")),
#             "Number_2": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
#             ).text.replace("#", "")),
#             "Number_3": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
#             ).text.replace("#", "")),
#             "Number_4": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
#             ).text.replace("#", "")),
#             "Number_5": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
#             ).text.replace("#", "")),
#             "Number_6": int(dv.find_element_by_xpath(
#                 "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
#             ).text.replace("#", ""))
#         }
#         print("Ky: " + str(objTic["KyQuay"]))
#         lstOut.append(objTic)

# with open('645.json', 'w') as outfile:
#     json.dump(lstOut, outfile)