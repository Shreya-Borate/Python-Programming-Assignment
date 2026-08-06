'''Write a Python program that performs a file backup every hour.

The program should:

1. Accept the source file path.
2. Accept the destination directory path.
3. Copy the source file to the destination directory.
4. Add the current date and time to the backup filename.
5. Write the backup operation details into:

backup_log.txt

Example backup filename:
Data_25_07_2026_16_30_00.txt

Use the shutil module for file copying.'''
import schedule
import time
import shutil
import datetime
import os

source = input("Enter source file path: ")
destination = input("Enter destination folder: ")

def Backup():

    current = datetime.datetime.now()
    timestamp = current.strftime("%d_%m_%Y_%H_%M_%S")

    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    backupfile = destination + "\\" + name + "_" + timestamp + ext

    shutil.copy(source, backupfile)

    logfile = open("backup_log.txt", "a")
    logfile.write("Backup completed successfully at ")
    logfile.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))
    logfile.write("\n")
    logfile.close()

    print("Backup completed successfully.")

schedule.every(1).hours.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)