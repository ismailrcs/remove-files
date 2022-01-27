from importlib.resources import path
import time
import os
import shutil

day=time.time()
os.path.exists(path)
if path.exists()==True:
    os.walk(path)
    os.path.join()
    ctime=os.stat(path).st_ctime
    if day >30 :
        os.remove(path)
    else :
        shutil.rmtree
    if path.exists()==False:
        print("Path not found")