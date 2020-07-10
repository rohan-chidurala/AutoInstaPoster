from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
import os, shutil
from distutils.dir_util import copy_tree
from Scripts.FilesScript import RenameAllFiles
from time import sleep


folder = 'PostingInfo'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))




root = Tk()
container = Frame(root)



UserNamesBox = []
PasswordsBox = []

UserNames = []
Passwords = []

BrowseButtons = []
FolderPaths = []


EnterNumberOfAccounts = Label(root, text='Number of accounts you want to have auto post for')
EnterNumberOfAccounts.pack(pady=20)

NumberOfAccounts = Entry(root, width = 10)
NumberOfAccounts.pack(pady=10)

NumberOfPostsADay = 0



column = []
AccountsCount = 1
def myClick():
    global AccountsCount
    try:
        
        AccountsCount = int(NumberOfAccounts.get())
        for widgets in root.winfo_children():
            widgets.destroy()
        for x in range(AccountsCount):

            AccountLabel = Label(root, text = "Account " + str(x+ 1))
            AccountLabel.grid(row = 0, column = x, pady = 10, padx = 5)
            
            UserName = Entry(root)
            UserName.insert(0,'Username')
            UserName.grid(row = 1, column =  x, pady = 20, padx =5)
            UserNamesBox.append(UserName)


            Password = Entry(root)
            Password.insert(0,'Password')
            Password.grid(row = 2, column =  x, pady = 20, padx =5)
            PasswordsBox.append(Password)

            
            FolderPathLabel = Label(master=root,text = '')
            FolderPathLabel.grid(row = 3, column =  x, pady = 20, padx =5)
            FolderPaths.append(FolderPathLabel)

            browsebutton = Button(text="Browse", command=browse_button)
            browsebutton.grid(row=4, column=x)
            BrowseButtons.append(browsebutton)

        DescriptionsLabel = Label(root, text= "Please Write Descriptions in each file for it")
        DescriptionsLabel.grid(row = 5, column =  2, pady = 20, padx =5)


        StartPostingButton = Button(root, text='Start Posting', command= StartPosting)
        StartPostingButton.grid(row = 100, column =  2, pady = 20, padx =5)


    except ValueError:
        CreateAcountsResponce.config(text = 'Please Put a integer in the input')
def CreateDataFiles(UserNames, Passwords, FolderPaths):
    global AccountsCount

    path = 'PostingInfo'
    UserNamesFile = open(path+'/UserNames.txt', 'a')
    PasswordsFile = open(path+'/Passwords.txt', 'a')

    for i in UserNames:
        UserNamesFile.write(i + '\n')

    for i in Passwords:
        PasswordsFile.write(i + '\n')



    for i in range(len(UserNames)):
        print(i)
        f=open(path+'/Image'+ str(i)+'_Descriptions.txt', 'w')
        f.close() 

        os.mkdir(path+'/Image'+str(i))
        original = FolderPaths[1].cget("text")
        target = path+'/Image'+str(i)

        copy_tree(original, target)


    print(FolderPaths[1].cget("text"))
    RenameAllFiles(AccountsCount)
    for widgets in root.winfo_children():
        widgets.destroy()
    BotText = Label(root, text = "Please proceed to the bot file and run when every you want or create a windows start command for automation for more info watch my video")
    BotText.pack()


def StartPosting():
    for i in UserNamesBox:
        UserNames.append(i.get())
    for i in PasswordsBox:
        Passwords.append(i.get())

    

    CreateDataFiles(UserNames,Passwords, FolderPaths )


def browse_button():
    
    filename = filedialog.askdirectory()
    FolderPaths[column[0]].config(text = filename)
def mouse(event):
    grid_info = event.widget.grid_info()
    print("row:", grid_info["row"], "column:", grid_info["column"])
    column.clear()
    column.append(grid_info["column"])
root.bind("<Button-1>", mouse)




CreateAcounts = Button(root, text="Create Accounts", command = myClick)
CreateAcounts.pack()

CreateAcountsResponce = Label(root, text='')
CreateAcountsResponce.pack(pady = 20)




root.mainloop()