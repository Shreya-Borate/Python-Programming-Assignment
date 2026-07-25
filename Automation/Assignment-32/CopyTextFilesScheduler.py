'''Write a Python program that copies all .txt files from one directory to another every ten minutes.

The program should:

• Accept source and destination directories
• Validate both directories
• Copy only .txt files
• Maintain a log of copied files
• Avoid terminating if one file cannot be copied'''

import schedule
import time
import shutil
import os

def CopyFiles(source, destination):

    logfile = open("CopyLog.txt", "a")

    for file in os.listdir(source):

        if file.endswith(".txt"):

            src = os.path.join(source, file)
            dest = os.path.join(destination, file)

            try:
                shutil.copy(src, dest)
                logfile.write(file + " copied successfully.\n")
            except Exception:
                logfile.write(file + " could not be copied.\n")

    logfile.close()

    print("Copy operation completed.")

def main():

    source = input("Enter source directory : ")
    destination = input("Enter destination directory : ")

    if not os.path.isdir(source) or not os.path.isdir(destination):
        print("Invalid directory.")
        return

    schedule.every(10).minutes.do(CopyFiles, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()