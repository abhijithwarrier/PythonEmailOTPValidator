# Programmer - python_scripts (Abhijith Warrier)

# Importing necessary packages
import random
import smtplib
import tkinter as tk
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidget():
    emailLabel = Label(root, text="ENTER YOUR EMAIL-ID : ", bg="deepskyblue3")
    emailLabel.grid(row=0, column=1, padx=5, pady=5)

    emailEntry = Entry(root, textvariable=emailid, width=30)
    emailEntry.grid(row=0, column=2, padx=5, pady=5)

    sendOTPbutton = Button(root, text="Send OTP", command=sendOTP, width=20)
    sendOTPbutton.grid(row=0, column=3, padx=5, pady=5)

    root.msgLabel = Label(root, bg="deepskyblue3")
    root.msgLabel.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

    otpLabel = Label(root, text="ENTER THE OTP : ", bg="deepskyblue3")
    otpLabel.grid(row=2, column=1, padx=5, pady=5)

    root.otpEntry = Entry(root, textvariable=otp, width=30, show="*")
    root.otpEntry.grid(row=2, column=2, padx=5, pady=5)

    validOTPbutton = Button(root, text="Validate OTP", command=validOTP, width=20)
    validOTPbutton.grid(row=2, column=3, padx=5, pady=5)

    root.otpLabel = Label(root, bg="deepskyblue3")
    root.otpLabel.grid(row=3, column=1, padx=5, pady=5, columnspan=3)

# Defining sendOTP() to generate and send OTP to user-input email-id
def sendOTP():
    # Storing digits from 0 to 9 as string in numbers variable & declaring empty string
    # variable named root.genOTP
    numbers = "0123456789"
    root.genOTP = ""
    # Fetching and storing user-input mail id in receiverEmail variable
    receiverEmail = emailid.get()

    # Generating 6-digits OTP
    for i in range(6):
        root.genOTP += numbers[int(random.random() * 10)]
    # Concatenating and Storing generated OTP with Message to be sent in otpMSG
    otpMSG = "YOUR OTP IS : " + root.genOTP

    # Creating instance of class MIMEMultipart()
    message = MIMEMultipart()
    # Storing the email details in respective fields
    message['FROM'] = "OTP VALIDATOR (python_scripts)"
    message['To'] = receiverEmail
    message['Subject'] = "OTP VALIDATION"
    # Attaching the otgMSG with MIME instance
    message.attach(MIMEText(otpMSG))

  # Creating a smtp session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Starting TLS for security
    smtp.starttls()
    # Authenticating the sender using the login() method
    smtp.login("sender's email-id", "sender's password")
    # Sending the email with Mulitpart message converted into string
    smtp.sendmail("sender's email-id", receiverEmail, message.as_string())
    # Terminating the session
    smtp.quit()

    # Formatting receiveEmail to replace(hide) mail id with *
    receiverEmail = '{}********{}'.format(receiverEmail[0:2], receiverEmail[-10:])
    # Displaying the success message
    root.msgLabel.config(text = "OTP HAS BEEN SENT TO " + receiverEmail)

# Defining validOTP() to validate user-input OTP mail with script generated OTP
def validOTP():
    # Storing user-input OTP
    userInputOTP = otp.get()
    # Storing system generated OTP
    systemOTP = root.genOTP

    # Validating OTP
    if userInputOTP == systemOTP:
        root.otpLabel.config(text="OTP VALIDATED SUCCESSFULLY")
    else:
        root.otpLabel.config(text="INVALID OTP")

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and disabling the resizing property
root.title("EmailOTP")
root.resizable(False, False)
root.config(background = "deepskyblue3")

# Creating tkinter variables
emailid = StringVar()
otp = StringVar()

# Calling the CreateWidgets() function with argument bgColor
CreateWidget()

# Defining infinite loop to run application
root.mainloop()
