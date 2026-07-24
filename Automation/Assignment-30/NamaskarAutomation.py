'''Write a Python program that creates a task which executes every day at 9:00 AM and prints:

Namaskar...

Use:
schedule.every().day.at("09:00").do(...)'''

import schedule
import time

def Display():
    print("Namaskar...")

schedule.every().day.at("09:00").do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)