'''Write a Python program that creates a new log file after every ten minutes.

The filename should contain the current date and time.

Example:

MarvellousLog_25_07_2026_16_30_00.txt

The file should contain:

Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM'''

import schedule
import time
import datetime

def CreateLog():

    current = datetime.datetime.now()

    filename = "MarvellousLog_" + current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    file = open(filename, "w")

    file.write("Log file created successfully.\n")
    file.write("Creation Time : ")
    file.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))

    file.close()

    print("Log file created.")

def main():

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()