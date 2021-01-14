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
    objTic = {
            "KyQuay": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[1]"
            ).text.replace("#", "")),
            "NgayQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[2]"
            ).text,
            "Number_1": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
            ).text.replace("#", "")),
            "Number_2": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
            ).text.replace("#", "")),
            "Number_3": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
            ).text.replace("#", "")),
            "Number_4": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
            ).text.replace("#", "")),
            "Number_5": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
            ).text.replace("#", "")),
            "Number_6": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
            ).text.replace("#", ""))
        }
    return objTic

def get655Data():
    dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655")
    objTic = {
            "KyQuay": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[1]"
            ).text.replace("#", "")),
            "NgayQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[2]"
            ).text,
            "Number_1": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
            ).text.replace("#", "")),
            "Number_2": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
            ).text.replace("#", "")),
            "Number_3": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
            ).text.replace("#", "")),
            "Number_4": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
            ).text.replace("#", "")),
            "Number_5": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
            ).text.replace("#", "")),
            "Number_6": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
            ).text.replace("#", "")),
            "Number_Bonus": int(dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[7]"
            ).text.replace("#", ""))
        }
    return objTic