'''Problem Statement

Design an automation script that accepts the name of a process as a command line argument and displays information about that process only.

The script should display the following details:

Process Name
Process ID (PID)
Username

Store the process information in a log file instead of displaying it on the console.'''

import sys
import Helper


def DisplayProcess(processName):

    processList = Helper.GetSpecificProcess(processName)

    if len(processList) == 0:
        print("Process not found.")
        return

    Helper.WriteLog("Automation.log", processList)

    print("Automation.log created successfully.")


def main():

    try:

        if len(sys.argv) != 2:
            print("Usage : python ProcInfo2.py <ProcessName>")
            return

        processName = sys.argv[1]

        DisplayProcess(processName)

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()