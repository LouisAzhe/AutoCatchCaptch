from selenium import webdriver
import os
import wget
import time
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import messagebox

def catch_picture(driver_path,url,xpath,folder_name,number,times):
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    # active chrome driver
    #chromedriver location
    driver = webdriver.Chrome(driver_path,chrome_options=chrome_options)
    #driver.get(url)

    # Max The Window
    driver.maximize_window()
    # open the page which has picture
    driver.get(url)

    path = os.path.join(folder_name)
    #os.mkdir(path)

    # for i in range(1,number+1):
    #     img = driver.find_element_by_xpath(xpath)
    #     save_as = os.path.join(path,folder_name+str(i)+'.jpg')
    #     #print(img.get_attribute("src"))
    #     wget.download(img.get_attribute("src"),save_as)
    #     time.sleep(times)
    #     driver.refresh()
    # print('Mission Complete!')
    # driver.close()
    # driver.quit()

driver_path = 'C:/temp/chromedriver.exe'
url = 'https://domestic.judicial.gov.tw/judbp/wkw/WHD9HN01/VERIFY_CODE_IMAGE.htm'
xpath = '/html/body/img'
folder_name = 'tax_new'
number = 10
times = 1

#main
catch_picture(driver_path,url,xpath,folder_name,number,times)

# messagebox.showinfo('Mission Complete!','Mission Complete!')