# import all necessary libraries

from tkinter import *
import random
import smtplib

# the main function starts here

OTP=str(random.randint(100000,999999))

subject='OTP Verification'
msg=f'Your OTP is: {OTP}'
print(type(msg))

# Function to Send OTP on Email
def send():

    email = smtplib.SMTP("smtp.office365.com", 587)
    email.starttls()
    Email_id = entry1.get()
    password = entry2.get()
    email.login("maurya111khushi@outlook.com", password)
    email.sendmail("maurya111khushi@outlook.com", Email_id, f'Subject:{subject}\n\n{msg}')
    email.quit()

# Working on the designing of the OTP Verification Project's Accessibility

# Create the main window
win=Tk()
win.geometry("700x400")
win.title("OTP VERIFICATION")

# Create GUI components
frame=Frame(win,width=700,height=20,bg="navy blue")
frame.grid(row=0,column=0)
frame=Frame(win,width=700,height=10,bg="thistle")
frame.grid(row=10,column=0)


Label(win,text="Enter Your Email-ID or User Name : ",font="Forte 17 ",fg="navy blue",bg="pink",width=30,height=1).place(x=10,y=80)

entry1=Entry(win,font="cambria 14",bd=3,width=25)
entry1.place(x=410,y=80)

Label(win,text="Enter Your Password : ",font="Forte 17 ",fg="navy blue",bg="pink",width=30,height=1).place(x=10,y=120)

entry2=Entry(win,font="cambria 14",bd=3,width=25)
entry2.place(x=410,y=120)


Button(win,text="Click to Send OTP",font="Forte 14 bold",bg="DarkSlateBlue",fg="white",bd=10,height=1,width=18,command=send).place(x=220,y=170)

Label(win,text="Enter the OTP : ",font="Forte 17 bold",fg="LavenderBlush",bg="DarkCyan",width=20,height=1).place(x=100,y=240)
Entry3 = Entry(win, font="Modern 16 bold", bg="pink", width=20, bd=4)
Entry3.place(x=400, y=240)

# Function to check the OTP is Right or Wrong
def submit():
    s = Entry3.get()
    if (s == str(OTP)):
        Label(win, text="Your OTP is verified!", font="Modern 17 bold", fg="MintCream", bg="DarkSlateBlue",width=25).place(x=230, y=340)
    else:
        Label(win, text="Your OTP is invalid!", font="Modern 17 bold", fg="MintCream", bg="DarkSlateBlue",width=25).place(x=230, y=340)

Button(win,text="Submit the OTP",font="Forte 14 bold",bg="DarkSlateBlue",fg="white",bd=10,height=1,width=18,command=submit).place(x=220,y=280)


# Run the main event loop
win.mainloop()







