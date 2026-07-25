'''Write a Python program that deletes all empty files from a specified directory every hour.

The program should:

• Scan the directory recursively
• Detect files whose size is zero bytes
• Delete the empty files
• Store deleted file paths in a log file
• Handle permission errors

Test the program only on a sample directory.'''

import schedule
import time
import os

def DeleteFiles(path):

    logfile = open("DeletedFilesLog.txt", "a")

    for folder, subfolders, files in os.walk(path):

        for file in files:

            filepath = os.path.join(folder, file)

            try:

                if os.path.getsize(filepath) == 0:

                    os.remove(filepath)

                    logfile.write(filepath + "\n")

                    print(filepath, "deleted.")

            except PermissionError:

                print("Permission denied :", filepath)

    logfile.close()

def main():

    path = input("Enter directory path : ")

    schedule.every(1).hours.do(DeleteFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()