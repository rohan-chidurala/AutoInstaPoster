
import os, shutil

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import urllib.request


driver = webdriver.Chrome()

driver.get('https://www.instagram.com/p/BuE82VfHRa6/')

userid_element = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a')[0].click()
time.sleep(2)

# here, you can see user list you want.
# you have to scroll down to download more data from instagram server.
# loop until last element with users table view height value.

users = []

height = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div").value_of_css_property("padding-top")
match = False
while match==False:
    lastHeight = height

    # step 1
    elements = driver.find_elements_by_xpath("//*[@id]/div/a")

    # step 2
    for element in elements:
        if element.get_attribute('title') not in users:
            users.append(element.get_attribute('title'))

    # step 3
    driver.execute_script("return arguments[0].scrollIntoView();", elements[-1])
    time.sleep(1)

    # step 4
    height = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div").value_of_css_property("padding-top")
    if lastHeight==height:
        match = True

print(users)
print(len(users))
driver.quit()