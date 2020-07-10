
import os, shutil

import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import urllib.request

import Scripts.FilesScript as FS



try:
    Usernames = FS.TXTtoList('PostingInfo/UserNames.txt')
    Passwords = FS.TXTtoList('PostingInfo/Passwords.txt')
except Exception:
    print('ERROR: you need to create the accounts first to do that you need to run app.py first.')

for i in range(len(Usernames)):

    WhatPassord = i

    username = Usernames[i]
    password = Passwords[i]


    AddToFile = True


    driver = webdriver.Chrome()


    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password) 
    driver.find_element_by_class_name("L3NKy").click()

    time.sleep(5)
    driver.get("https://www.instagram.com/"+username +"/saved/")


    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    match = False
    while(match == False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        if lastCount == lenOfPage:
            match = True


    posts = []
    links = driver.find_elements_by_tag_name('a')

    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post:
            posts.append(post)
        
    print(posts)

    download_url = ''

    try:
        Img_Path = 'PostingInfo/Image' + str(i) + '/'

        Video_Path = 'UserDownloads/'+username+'_Downloads/Videos/'
        os.makedirs(Video_Path)
    except Exception:
        pass

    for post in posts:
        driver.get(post)
        shortcode = driver.current_url.split("/")[-2]


        # download_url = driver.find_elements_by_class_name('FFVAD')[0].get_attribute("src")
        # urllib.request.urlretrieve(download_url, Img_Path +"{}.jpg".format(shortcode))
        
        # type = driver.find_element_by_xpath('//meta[@property="og:type"]').get_attribute("content")
        try:
            print ('Working')
            time.sleep(2)
            driver.find_element_by_class_name("  _6CZji ").click()
            print('Working')
            driver.find_element_by_class_name(" POSa_  ").click()

            lenOfPost = driver.find_elements_by_class_name("JSZAJ  _3eoV-  IjCL9  WXPwG").click()
            
            for i in range(len(lenOfPost)):
                try:
                    download_url = driver.find_elements_by_class_name('FFVAD')[0].get_attribute("src")
                    try:
                        urllib.request.urlretrieve(download_url, Img_Path +"{}.jpg".format(shortcode+ str(i)))
                        print(download_url)
                    except Exception:
                        pass
                
                
                except Exception:

                    download_url = driver.find_elements_by_class_name('tWeCl')[0].get_attribute("src")
                    try:
                        urllib.request.urlretrieve(download_url, Video_Path +"{}.mp4".format(shortcode + str(i)))
                        print(download_url)
                    except Exception:
                        pass 
                    

        except Exception:

            try:
                download_url = driver.find_elements_by_class_name('FFVAD')[0].get_attribute("src")
                try:
                    urllib.request.urlretrieve(download_url, Img_Path +"{}.jpg".format(shortcode))
                    print(download_url)
                except Exception:
                    pass
            
            
            except Exception:

                download_url = driver.find_elements_by_class_name('tWeCl')[0].get_attribute("src")
                try:
                    urllib.request.urlretrieve(download_url, Video_Path +"{}.mp4".format(shortcode))
                    print(download_url)
                except Exception:
                    pass 
                    
        
    #driver.close()
    
