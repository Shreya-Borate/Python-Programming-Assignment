'''Design an automation script that accepts the directory name and email address from the command line.

If the specified directory does not exist, create it. Generate a log file inside that directory containing information about all running processes.

The log file should contain:

Process Name
Process ID (PID)
Username

After creating the log file, send it as an email attachment to the specified email address.'''
import sys
import os
import Helper
import MailSender


def CreateDirectory(directoryName):

    if not os.path.exists(directoryName):
        os.mkdir(directoryName)

    return os.path.join(directoryName, "Automation.log")


def CreateLog(directoryName):

    processList = Helper.GetProcessInfo()

    if len(processList) == 0:
        print("No running processes found.")
        return None

    fileName = CreateDirectory(directoryName)

    Helper.WriteLog(fileName, processList)

    print("Log file created successfully.")

    return fileName


def main():

    try:

        if len(sys.argv) != 3:
            print("Usage : python ProcInfoMail.py <DirectoryName> <EmailID>")
            return

        directoryName = sys.argv[1]
        receiverEmail = sys.argv[2]

        fileName = CreateLog(directoryName)

        if fileName != None:
            MailSender.SendEmail(receiverEmail, fileName)

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()