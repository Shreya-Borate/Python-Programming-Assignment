# ----------------------------------------------------------
# File Name    : MailSender.py
# Description  : Common Email Module
# Author       : Shreya Borate
# ----------------------------------------------------------

import os
import smtplib
from email.message import EmailMessage


# ----------------------------------------------------------
# Function Name : SendEmail
# Description   : Sends log file through email
# ----------------------------------------------------------
def SendEmail(receiverEmail, fileName):

    senderEmail = input("Enter Sender Gmail ID : ")
    appPassword = input("Enter Gmail App Password : ")

    try:

        if not os.path.exists(fileName):
            print("Attachment file does not exist.")
            return

        message = EmailMessage()

        message["Subject"] = "Process Automation Log File"
        message["From"] = senderEmail
        message["To"] = receiverEmail

        message.set_content(
            "Hello,\n\nPlease find the attached Process Automation Log File.\n\nThank You."
        )

        with open(fileName, "rb") as file:
            fileData = file.read()
            fileNameOnly = os.path.basename(fileName)

        message.add_attachment(
            fileData,
            maintype="application",
            subtype="octet-stream",
            filename=fileNameOnly
        )

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(senderEmail, appPassword)

        server.send_message(message)

        server.quit()

        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication Failed. Check Gmail ID or App Password.")

    except FileNotFoundError:
        print("Attachment file not found.")

    except Exception as e:
        print("Error :", e)