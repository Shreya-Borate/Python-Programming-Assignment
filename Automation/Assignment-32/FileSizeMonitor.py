'''Write a Python program that monitors the size of a specified file every 30 seconds.

Write the following details into:

FileSizeLog.txt

• File path
• File size in bytes
• Date and time

Handle the situation where the file does not exist.'''

import schedule
import time
import datetime
import os

def Monitor(path):

    file = open("FileSizeLog.txt", "a")

    current = datetime.datetime.now()

    if os.path.exists(path):

        size = os.path.getsize(path)

        file.write("File Path : " + path + "\n")
        file.write("File Size : " + str(size) + " bytes\n")
        file.write("Date and Time : " + current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

        print("Log Updated")

    else:

        file.write("File not found : " + path + "\n")
        file.write("Date and Time : " + current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

        print("File does not exist.")

    file.close()

def main():

    path = input("Enter file path : ")

    schedule.every(30).seconds.do(Monitor, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()