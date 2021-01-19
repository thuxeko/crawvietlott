from selenium import webdriver
from datetime import datetime,date

chromePath = "D:/chromedriver/chromedriver.exe"
dv = webdriver.Chrome(executable_path=chromePath)

dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655")

objTic = {
            "KyQuay": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[1]/div[1]/div/h5/b[1]"
            ).text.replace("#", "")),
            "NgayQuay": datetime.strptime(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[1]/div[1]/div/h5/b[2]"
            ).text, '%d/%m/%Y'),
            "Number_1": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[1]"
            ).text.replace("#", "")),
            "Number_2": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[2]"
            ).text.replace("#", "")),
            "Number_3": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[3]"
            ).text.replace("#", "")),
            "Number_4": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[4]"
            ).text.replace("#", "")),
            "Number_5": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[5]"
            ).text.replace("#", "")),
            "Number_6": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[6]"
            ).text.replace("#", "")),
            "Number_Bonus": int(dv.find_element_by_xpath(
                "//*[@id='divLeftContent']/div/div[2]/div/div[1]/span[7]"
            ).text.replace("#", ""))
        }

print(objTic)