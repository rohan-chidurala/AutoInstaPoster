import os
from pathlib import Path
import time 
import datetime
import platform
import glob
import shutil
import csv
import random
import sys
def RandomDescriptions(num):

    with open('PostingInfo/Image'+ str(num) +'_Descriptions.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(data)
    try:    
        randInt =  random.randint(0,len(data)-1)
    except Exception:


        sys.exit()
    final = data[randInt][0][:-2]
    final = final[3:]

    return(final)



def TXTtoList(filename):

    a_file = open(filename, "r")

    list_of_lists = []
    for line in a_file:
        line = line[:-1]
        list_of_lists.append(line)

    a_file.close()

    return (list_of_lists)



def  SortByDate(Name):
    path = Name + '/'
    filenames = glob.glob(path+"*")
    dictionary = {}
    global files 
    files = []

    def win_file(file):
        return datetime.datetime.fromtimestamp(os.path.getctime(file))

    for file in filenames:
        
        file_time = win_file(file)
        file_date = file_time.strftime("%d.%m.%y %H.%M.%S.%f")
        file_date = file_date[::-1]
        files.append(file)
        dictionary[file] = file_date

    for key,value in dictionary.items():
        fileFormat = key[-4:]
        if fileFormat == '.jpg':
            os.rename(key, path +value + '.jpg')
        elif fileFormat == '.png':
            os.rename(key, path +value + '.jpg')
        elif fileFormat == '.mp4':
            os.rename(key, path +value + '.mp4')
        else:
            os.rename(key, path +value)
    print(files)

def win_file(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))

def  SortByNumber(Name):
    path = Name + '/'
    filenames = glob.glob(path+"*")
    dictionary = {}

    

    i = 0
    for file in filenames:
        file_date = str(i)
        i +=1

        dictionary[file] = file_date

    for key,value in dictionary.items():
        os.rename(key, path +value + '.jpg')



def RenameAllFiles(num):

    for i in range(num):
        path = 'PostingInfo'
        SortByDate(path+'/Image'+str(i))
        SortByNumber(path+'/Image'+str(i))
        if len(os.listdir(path+'/Image'+str(i)) ) == 0:
            print("ERROR: Image File " + str(i) +" is empty please refill")
            sys.exit()





