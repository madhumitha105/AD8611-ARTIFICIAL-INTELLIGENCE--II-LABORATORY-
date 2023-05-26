from tkinter import *
import pyperclip    #to copy password into clipboard
import random   #to generate random password

init = Tk() #initializing tkinter
#setting the width and height of the GUI
init.geometry("400x400")    # x is small case here
init.title("Password Generator")

passStr = StringVar()   #declaring a variable of string type and this variable will be used to store the password generated
passLen = IntVar()  #declaring a variable of integer type which will be used to store the length of the password.
passLen.set(0)  #setting the length of the password to zero initially

# function to generate the password
def generate():
    #storing the keys in the list which will be used the password
    pass1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
            'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
            '1','2','3','4','5','6','7','8','9','0','','!','@','#','$','%','^','&','*','(',')']
    password = ''   #declaring the empty string

    #loop to generate the random password of the length entered by the user
    for x in range(passLen.get()):
        password = password + random.choice(pass1)

    #setting the password to the entry widget
    passStr.set(password)

#function to copy the password to the clipboard
def copyToClipboard():
    random_password = passStr.get()
    pyperclip.copy(random_password)

#Creating a text label widget
Label(init, text = "Password Generator", font="calibri 20 bold").pack()
Label(init, text="Enter password length").pack(pady=3)

#creating a entry widget to take password length entered by the user
Entry(init, textvariable=passLen).pack(pady=3)

# button to call the generate function
Button(init,text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(init, textvariable=passStr).pack(pady=3)
#buttom to call the copyToClipboard function
Button(init, text="Copy to clipboard",command=copyToClipboard).pack()

init.mainloop() #mainloop() is an infinte loop used to run the application when it's ready state