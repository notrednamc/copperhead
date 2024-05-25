#!C:\Python27\python.exe
import os
import os.path
import subprocess

targetList = ["10.10.30.10", "127.0.0.1", "10.10.10.10", "10.10.10.20",]
cutList = []
# print targetList

def netUse(ip_addr):
    conn = subprocess.call("net use \\\\" + ip_addr + "\\IPC$ /USER:echonetadmin M1ch@elA")
    return conn

def checkFile(ip_addr):
    check = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\writekl.exe")
    return check

for target in targetList:
    try:
        ping = os.system("ping -n 1 " + target + " > nul")
    except Exception as e:
        print "Error: " + e
    else:
        if ping == 0:
            print "Successful ping to " + target
            if netUse(target):
                if checkFile(target):
                    print "remove files"
                else:
                    print "copy files over"
        if ping == 1:
            print "ErrorCode: 1. ## " + target + " will be removed from target list"
            cutList.append(target)
            continue
            targetList.remove(target)
        elif ping == 2:
            print "ErrorCode: 2. ## " + target + " will be removed from target list"
            cutList.append(target)
            continue

# print cutList
for item in cutList:
    targetList.remove(item)

print targetList