import win32com.client as w32
import random

def verifNum(): #generates a verification number
    num=random.randint(1,999999) 
    while len(num)<6:
        num="0"+str(num) #if number is less than 6 digits, add needed zeros at the front
    return num

print("Please enter your email")
userMailInput=input()

outlookApp = w32.Dispatch("Outlook.Application") #creates a variable to store the connection instance
olNS = outlookApp.GetNameSpace("MAPI")

mail = outlookApp.CreateItem(0)
mail.Subject = "Verification Email" #email subject
mail.BodyFormat = 1 #the format of the email's body will be set to plain text
mail.Body = f"The verification code for your account is {verifNum()}" #contents of the email
mail.To = userMailInput #recepient of the email

mail.Display() #shows the email before sending
mail.Save() #saves the message as a draft
mail.Send() #sends the email

print("A verification email has been sent to your inbox.")