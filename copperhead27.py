#!C:\Python27\python.exe
import os
import os.path
import subprocess
import shutil

targetList = ["10.10.30.10"]
#targetList = ["10.10.30.10", "127.0.0.1", "10.10.10.10", "10.10.10.20",]
cutList = []
# print targetList

def netUse(ip_addr):
    conn = subprocess.call("net use \\\\" + ip_addr + "\\IPC$ /USER:echonetadmin M1ch@elA")
    # winCMD = 'NET USE ' + networkPath + ' /User:' + user + ' ' + password
    # subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)
    return conn

def checkFile(ip_addr):
    check = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\writekl.exe")
    return check

def checkFile2(ip_addr):
    check = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\testupload1.exe")
    return check

def checkFile3(ip_addr):
    check = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\testupload1.lnk")
    return check

def copyFile(ip_addr):
    # copy = subprocess.call("copy testupload1.exe \\\\" + ip_addr + "\\C$\\Windows\\")
    copy = shutil.copy2("testupload1.exe", "\\\\" + ip_addr + "\\C$\\Windows\\")
    return copy

for target in targetList:
    try:
        ping = os.system("ping -n 1 " + target + " > nul")
    except Exception as e:
        print "Error: " + e
    else:
        if ping == 0:
            print "Successful ping to " + target
            if netUse(target) == 0:
                if checkFile(target) != 0:
                    print "remove files"
                    os.remove("\\\\" + target + "\\C$\\Windows\\writekl.exe")
                if checkFile2(target) != 0:
                    print "remove files2"
                    os.remove("\\\\" + target + "\\C$\\Windows\\testupload1.exe")
                #if checkFile3(target) != 0:
                #    print "remove link"
                #    os.remove("\\\\" + ip_addr + "\\C$\\")
                print "copy files"
                #if copyFile(target) == 0:
                    #print "WIN Again"
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