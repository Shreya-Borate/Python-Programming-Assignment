'''Design an automation script that displays information about all running processes in the system.

The script should collect and store the following details of each running process:

Process Name
Process ID (PID)
Username

Instead of displaying the information on the console, store all the process information in a log file.'''
import sys
import Helper


def DisplayProcesses():

    processList = Helper.GetProcessInfo()

    if len(processList) == 0:
        print("No running processes found.")
        return

    Helper.WriteLog("Automation.log", processList)

    print("Automation.log created successfully.")


def main():

    try:

        if len(sys.argv) != 1:
            print("Usage : python ProcInfo1.py")
            return

        DisplayProcesses()

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()