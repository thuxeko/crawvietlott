from selenium import webdriver
from time import sleep
import json

chromePath = "D:/chromedriver/chromedriver.exe"
dv = webdriver.Chrome(executable_path=chromePath)

dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655")

lstOut = []
# Wait load page
for x in range(526):
    if x == 0:
        objTic = {
            "KyQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div[1]/div/h5/b[1]"
            ).text,
            "NgayQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div[1]/div/h5/b[2]"
            ).text,
            "Number_1": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
            ).text,
            "Number_2": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
            ).text,
            "Number_3": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
            ).text,
            "Number_4": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
            ).text,
            "Number_5": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
            ).text,
            "Number_6": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
            ).text,
            "Number_Bonus": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[7]"
            ).text
        }
        print("Ky: " + objTic["KyQuay"])
        lstOut.append(objTic)
    else:
        prButton = dv.find_element_by_xpath(
            "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[2]/a[1]"
        )
        prButton.click()

        sleep(5)

        objTic = {
            "KyQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[1]"
            ).text,
            "NgayQuay": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/h5/b[2]"
            ).text,
            "Number_1": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[1]"
            ).text,
            "Number_2": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[2]"
            ).text,
            "Number_3": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[3]"
            ).text,
            "Number_4": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[4]"
            ).text,
            "Number_5": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[5]"
            ).text,
            "Number_6": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[6]"
            ).text,
            "Number_Bonus": dv.find_element_by_xpath(
                "/html/body/div[6]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/span[7]"
            ).text
        }
        print("Ky: " + objTic["KyQuay"])
        lstOut.append(objTic)

with open('data655.json', 'w') as outfile:
    json.dump(lstOut, outfile)