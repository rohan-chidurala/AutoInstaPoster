from instabot import Bot 
import Scripts.FilesScript as FS
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import autoit
import time
from selenium.webdriver.common.keys import Keys





try:
    Usernames = FS.TXTtoList('PostingInfo/UserNames.txt')
    Passwords = FS.TXTtoList('PostingInfo/Passwords.txt')
except Exception:
    print("ERROR: please run app.py first")





FS.RenameAllFiles(len(Usernames))
temp= FS.files

for i in range(len(Usernames)):


    username = Usernames[i]
    password = Passwords[i]


    description = FS.RandomDescriptions(i)

    mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options)


    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password) 
    driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button""").click()

    time.sleep(2)

    driver.get('https://www.instagram.com/' + username)


    try:
        ImagePath =  'PostingInfo/Image' + str(i)+ '/' + str(0) + '.jpg'
        temp = os.path.realpath(ImagePath)
    except Exception:
        ImagePath =  'PostingInfo/Image' + str(i)+ '/' + str(0) + '.mp4'
    
    print (ImagePath)

    dir_path = os.path.realpath(ImagePath)
    print(dir_path)


    ActionChains(driver).move_to_element( driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]""")).click().perform()
    handle = "[CLASS:#32770; TITLE:Open]"
    autoit.win_wait(handle, 3)
    autoit.control_set_text(handle, "Edit1", dir_path)
    autoit.control_click(handle, "Button1")

    time.sleep(2)

    driver.find_element_by_xpath("""//*[@id="react-root"]/section/div[1]/header/div/div[2]/button""").click()

    time.sleep(2)

    txt = driver.find_element_by_class_name('_472V_')
    txt.send_keys('')
    txt = driver.find_element_by_class_name('_472V_')
    txt.send_keys(description) # Descrition
    txt.send_keys(Keys.ENTER)

    driver.find_element_by_xpath("""//*[@id="react-root"]/section/div[1]/header/div/div[2]/button""").click()


    time.sleep(5)

    os.remove(ImagePath)
    driver.close()
    