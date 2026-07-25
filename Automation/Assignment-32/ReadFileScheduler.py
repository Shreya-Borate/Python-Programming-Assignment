'''Write a Python program that reads and displays the contents of a specified text file every minute.

Handle the following conditions:

• File does not exist
• File is empty
• Permission is denied
• File cannot be opened'''

import schedule
import time

def ReadFile(filename):

    try:

        file = open(filename, "r")

        data = file.read()

        if len(data) == 0:
            print("File is empty.")
        else:
            print(data)

        file.close()

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except Exception:
        print("File cannot be opened.")

def main():

    filename = input("Enter file name : ")

    schedule.every(1).minutes.do(ReadFile, filename)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()