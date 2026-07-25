'''Write a Python program that accepts a directory name from the user and counts the number of files inside it every five minutes.

Write the result into:

DirectoryCountLog.txt

Each entry should contain:

• Directory path
• Number of files
• Date and time'''
import schedule
import time
import os
import datetime

def CountFiles(path):

    count = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path, item)

        if os.path.isfile(fullpath):
            count += 1

    current = datetime.datetime.now()

    file = open("DirectoryCountLog.txt", "a")

    file.write("Directory : " + path + "\n")
    file.write("Number of Files : " + str(count) + "\n")
    file.write("Date and Time : " + current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

    file.close()

    print("Log Updated Successfully.")

def main():

    path = input("Enter directory path : ")

    schedule.every(5).minutes.do(CountFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()