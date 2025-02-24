import os
import sys
import time


print(sys.argv)
os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\windows'), 'temp']))
time.sleep(5)
