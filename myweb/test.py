from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

classurl = "https://hngs.peixunyun.cn/#/loginrealname?redirect=%2Fhomepage"
userid = "18684859553"
passwd = "19980201Ych"

s1 = Service(r"C:\Users\37770\Desktop\math\myweb\msedgedriver.exe")
browser = webdriver.Edge(service=s1)
browser.get(classurl)
browser.maximize_window()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/div[1]/div/div[1]/input').send_keys(userid)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/div[2]/div/div[1]/input').send_keys(passwd)
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/button').click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="a-link"]/div[2]/div[3]/div/button').click()
time.sleep(5)

x_path_zhankai = '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[myreplace]/div[2]/div[2]/div'

for i in range(1, 6):
    browser.find_element(By.XPATH, x_path_zhankai.replace("myreplace", str(i))).click()
    time.sleep(1)

xpath_l = [
    '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[6]/div/button',
    '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[5]/td[6]/div/button',
    '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[6]/td[6]/div/button',
    '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[7]/td[6]/div/button',
]

for x in xpath_l:
    browser.find_element(By.XPATH, x).click()
    while 1:
        pass
