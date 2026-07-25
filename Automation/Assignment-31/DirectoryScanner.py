'''Write a Python program that scans a specified directory every minute.

The task should display:

• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning

Use the os module.

Example Output:

Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM'''

import schedule
import time
import os
import datetime

def ScanDirectory(path):

    files = 0
    directories = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path, item)

        if os.path.isfile(fullpath):
            files += 1
        elif os.path.isdir(fullpath):
            directories += 1

    current = datetime.datetime.now()

    print("Directory Scanned :", path)
    print("Total Files :", files)
    print("Total Subdirectories :", directories)
    print("Scan Time :", current.strftime("%d-%m-%Y %I:%M:%S %p"))
    print()

def main():

    path = input("Enter directory path : ")

    schedule.every(1).minutes.do(ScanDirectory, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()