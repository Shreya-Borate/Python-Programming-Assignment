'''Write a Python program that accepts:

• A message from the user.

• A time interval in seconds.

Schedule the program to display the message repeatedly after the specified interval.

Example Input:

Enter message: Jay Ganesh
Enter interval in seconds: 5

Expected Output:

Jay Ganesh
(every five seconds)

Validate that the interval is greater than zero.'''

import schedule
import time

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval <= 0:
    print("Interval must be greater than zero.")
else:

    def Display():
        print(message)

    schedule.every(interval).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)