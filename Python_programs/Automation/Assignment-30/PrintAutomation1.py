'''Write a Python program that prints:

Jay Ganesh...

every two seconds.

Use:
schedule.every(2).seconds.do(...)'''
import schedule
import time

def Display():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(Display)

while True:
    schedule.run_pending()
    time.sleep(1)