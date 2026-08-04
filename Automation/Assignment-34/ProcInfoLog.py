'''Design an automation script that accepts the directory name from the command line.

If the specified directory does not exist, create it. Then create a log file inside that directory containing information about all running processes.

The log file should contain:

Process Name
Process ID (PID)
Username'''
import sys
import os
import Helper


def CreateDirectory(directoryName):

    if not os.path.exists(directoryName):
        os.mkdir(directoryName)

    return os.path.join(directoryName, "Automation.log")


def CreateLog(directoryName):

    processList = Helper.GetProcessInfo()

    if len(processList) == 0:
        print("No running processes found.")
        return

    fileName = CreateDirectory(directoryName)

    Helper.WriteLog(fileName, processList)

    print("Log file created successfully.")
    print("Location :", fileName)


def main():

    try:

        if len(sys.argv) != 2:
            print("Usage : python ProcInfoLog.py <DirectoryName>")
            return

        directoryName = sys.argv[1]

        CreateLog(directoryName)

    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()