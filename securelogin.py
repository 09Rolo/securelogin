import time
import ctypes
import os
import subprocess
import shutil

iconsetted = False
currdict = os.getcwd()
dict = str(open(f"{currdict}/directory.txt", "r").read())
dict = dict.replace("\\", "/")

while 1 == 1:
    time.sleep(9)

    process_name='LogonUI.exe'
    callall='TASKLIST'
    outputall=subprocess.check_output(callall)
    outputstringall=str(outputall)

    if process_name in outputstringall:
        print("L")
        if os.path.exists(f'{dict}/imhere'):
            iconsetted = False
            shutil.rmtree(f'{dict}/imhere', ignore_errors=True)
    else:
        if dict == None:
            print("Nincs asztal hely megadva. A directory fileba másold be az asztal helyét (pl: C:/-Rolo-/Asztal)")
        else:
            time.sleep(3)

            if os.path.exists(f'{dict}/imhere'):
                if (iconsetted == False):
                    try:
                        iconsetted = True

                        shutil.copy(f"{os.getcwd()}/ficon.ico", f"{dict}/imhere")

                        with open(f"{dict}/imhere/desktop.ini", "w") as file:
                            file.write(f"[.ShellClassInfo]\nIconFile=ficon.ico\nIconResource=" + dict.replace("/", "\\") + "\\imhere\\ficon.ico,0")
                            file.close()

                        os.system(f'attrib +s "{dict}/imhere"')
                        os.system(f'attrib +s +h "{dict}/imhere/desktop.ini"')
                    except:
                        print("")

            else:
                ctypes.windll.user32.LockWorkStation()
