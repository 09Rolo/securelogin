import time
import ctypes
import os
import subprocess


currdict = os.getcwd()
dict = str(open(f"{currdict}/directory.txt", "r").read())

while 1 == 1:
    time.sleep(9)

    process_name='LogonUI.exe'
    callall='TASKLIST'
    outputall=subprocess.check_output(callall)
    outputstringall=str(outputall)

    if process_name in outputstringall:
        print("L")
        if os.path.exists(f'{dict}/imhere'):
            os.rmdir(f'{dict}/imhere')
    else:
        if dict == None:
            print("Nincs asztal hely megadva. A directory fileba másold be az asztal helyét (pl: C:/-Rolo-/Asztal) (Ha lehet ne használj \\ -t, inkább /-t, ugyan az)")
        else:
            time.sleep(3)

            if os.path.exists(f'{dict}/imhere'):
                print("")
            else:
                ctypes.windll.user32.LockWorkStation()
