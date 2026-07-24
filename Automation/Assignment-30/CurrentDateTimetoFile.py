'''Write a Python program that schedules a task that executes every five minutes.

The task should write the current date and time into a file named:

Marvellous.txt

New entries should be appended without removing previous entries.'''

import schedule
import time
import datetime

def WriteFile():
    file = open("Marvellous.txt", "a")

    current = datetime.datetime.now()

    file.write("Task executed at : ")
    file.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))
    file.write("\n")

    file.close()

schedule.every(5).minutes.do(WriteFile)

while True:
    schedule.run_pending()
    time.sleep(1)