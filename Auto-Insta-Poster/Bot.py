from instabot import Bot 
import Scripts.FilesScript as FS
import os
from selenium import webdriver
import time

bot = Bot()

Usernames = FS.TXTtoList('PostingInfo/UserNames.txt')
Passwords = FS.TXTtoList('PostingInfo/Passwords.txt')




print(Usernames)
print(Passwords)


FS.RenameAllFiles(len(Usernames))

print('Please Wait this might may take some time please have some wait for sometime')

for i in range(len(Usernames)):

    username = Usernames[i]
    password = Passwords[i]

    print(username)
    print(password)




    ImagePath = 'PostingInfo/Image' + str(i)+ '/' + str(0) + '.jpg'

    bot.login(username = username,  password = password) 

    
    bot.upload_photo(ImagePath, caption ="Technical Scripter Event 2019") 

    CanPass = False
    try:
        os.remove(ImagePath + '.REMOVE_ME')
    except Exception:

        while CanPass == False:
            bot.upload_photo(ImagePath, caption ="Technical Scripter Event 2019") 
            try:
                os.remove(ImagePath + '.REMOVE_ME')
                CanPass = False
            except Exception:
                CanPass = True
                pass
    bot.logout() 

