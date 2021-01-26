from selenium import webdriver
from time import sleep
import json

chromePath = "D:/chromedriver/chromedriver.exe"
dv = webdriver.Chrome(executable_path=chromePath)

dv.get("https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655")

lstOut = []
# Wait load page
for x in range(527):
    if x == 0:
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
            "Number_6": int(objBall[5].text),
            "Number_Bonus": int(objBall[6].text)
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
            "Number_1": int(objBallN[0].text),
            "Number_2": int(objBallN[1].text),
            "Number_3": int(objBallN[2].text),
            "Number_4": int(objBallN[3].text),
            "Number_5": int(objBallN[4].text),
            "Number_6": int(objBallN[5].text),
            "Number_Bonus": int(objBallN[6].text)
        }
        print("Ky: " + str(objTic["KyQuay"]))
        lstOut.append(objTic)

with open('655.json', 'w') as outfile:
    json.dump(lstOut, outfile)