'''Write a Python program that displays the current date and time after every one minute.

Use the datetime module.

Expected Output:

Current Date and Time: 25-07-2026 04:30:00 PM'''

import schedule
import time
import datetime

def DisplayTime():
    current = datetime.datetime.now()
    print("Current Date and Time :", current.strftime("%d-%m-%Y %I:%M:%S %p"))

schedule.every(1).minutes.do(DisplayTime)

while True:
    schedule.run_pending()
    time.sleep(1)