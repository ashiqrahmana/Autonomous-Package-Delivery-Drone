import threading
import time
import os
class myThread(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.cmd = command

    def run(self):
        print("Starting " + self.cmd)
        os.system(self.cmd)
        print("Exiting " + self.cmd)


thread1 = myThread("python3 bash_code.py")
thread2 = myThread("python3 main_gui.py")

thread1.start()
time.sleep(10)
thread2.start()