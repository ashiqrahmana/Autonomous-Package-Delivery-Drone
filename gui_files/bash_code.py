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


thread11 = myThread("cd \n bash drone.sh")
thread12 = myThread("cd \n bash mavros.sh")

thread11.start()
time.sleep(20)
thread12.start()
