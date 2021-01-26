from selenium import webdriver
from time import sleep
import json
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

dv = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def get645Data():
    dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645")

    objBall = dv.find_elements_by_xpath("//*[contains(@class, 'bong_tron')]")
    objText = dv.find_elements_by_xpath("//div[@class='chitietketqua_title']/h5/b")

    objTic = {
            "KyQuay": int(objText[0].text.replace("#", "")),
            "NgayQuay": objText[1].text,
            "Number_1": int(objBall[0].text),
            "Number_2": int(objBall[1].text),
            "Number_3": int(objBall[2].text),
            "Number_4": int(objBall[3].text),
            "Number_5": int(objBall[4].text),
            "Number_6": int(objBall[5].text)
        }
    return objTic

def get655Data():
    dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655")

    objText = dv.find_elements_by_xpath("//div[@class='chitietketqua_title']/h5/b")
    objBall = dv.find_elements_by_xpath("//*[contains(@class, 'bong_tron')]")
    
    objTic = {
            "KyQuay": int(objText[0].text.replace("#", "")),
            "NgayQuay": objText[1].text,
            "Number_1": int(objBall[0].text),
            "Number_2": int(objBall[1].text),
            "Number_3": int(objBall[2].text),
            "Number_4": int(objBall[3].text),
            "Number_5": int(objBall[4].text),
            "Number_6": int(objBall[5].text),
            "Number_Bonus": int(objBall[6].text)
        }
    return objTic