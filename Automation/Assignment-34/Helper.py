# ----------------------------------------------------------
# File Name    : Helper.py
# Description  : Common helper module for Process Automation
# Author       : Shreya Borate
# ----------------------------------------------------------

import psutil
from datetime import datetime


# ----------------------------------------------------------
# Function Name : GetProcessInfo
# Description   : Returns information about all running processes
# ----------------------------------------------------------
def GetProcessInfo():

    processList = []

    try:
        for process in psutil.process_iter(['pid', 'name', 'username']):
            try:
                processList.append(process.info)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

    except Exception as e:
        print("Error :", e)

    return processList


# ----------------------------------------------------------
# Function Name : GetSpecificProcess
# Description   : Returns information about a specific process
# ----------------------------------------------------------
def GetSpecificProcess(processName):

    processList = []

    try:
        for process in psutil.process_iter(['pid', 'name', 'username']):

            try:
                if process.info['name'] is not None:

                    if process.info['name'].lower() == processName.lower():
                        processList.append(process.info)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

    except Exception as e:
        print("Error :", e)

    return processList


# ----------------------------------------------------------
# Function Name : WriteLog
# Description   : Writes process information into log file
# ----------------------------------------------------------
def WriteLog(fileName, processList):

    try:

        with open(fileName, "w") as file:

            file.write("=" * 70 + "\n")
            file.write("              Process Automation Log\n")
            file.write("=" * 70 + "\n")
            file.write("Generated On : " + str(datetime.now()) + "\n")
            file.write("Total Processes : " + str(len(processList)) + "\n")
            file.write("=" * 70 + "\n\n")

            for process in processList:

                file.write(f"Process Name : {process['name']}\n")
                file.write(f"PID          : {process['pid']}\n")
                file.write(f"Username     : {process['username']}\n")
                file.write("-" * 70 + "\n")

    except Exception as e:
        print("Unable to create log file :", e)