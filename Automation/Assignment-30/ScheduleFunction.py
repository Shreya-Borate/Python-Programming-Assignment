'''Write a Python program that schedules a function to print:

Coding Kar..!

every 30 minutes.'''
import schedule
import time

def Display():
    print("Coding Kar..!")

schedule.every(30).minutes.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)