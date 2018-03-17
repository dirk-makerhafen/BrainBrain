import os,sys,threading
import p2pNode

import time

print("# USAGE: ")
print("")
print(" node = p2pNode('yourip',False)")
print(" node.start()")


from brainweb.models import Individual
from django.db import connection
print(len(connection.queries))
i = Individual.objects.all()[0:4]
print(i)
def runThread(cmd):
    while True:
        os.system(cmd)
        print("thread '%s' exited " % cmd)
        time.sleep(5)
        
def work(nrOfthread):
    cmd = "python3 p2pNode.py"    
    t = threading.Thread(target=runThread,args=[cmd])
    t.daemon = True
    t.start()

    for _ in range(0,nrOfthread-1):
        cmd = "python3 run-google-testcases.py run random"
        t = threading.Thread(target=runThread,args=[cmd])
        t.daemon = True
        t.start()
    cmd = "python3 advtain.py"    
    t = threading.Thread(target=runThread,args=[cmd])
    t.daemon = True
    t.start()

import IPython
IPython.embed()
