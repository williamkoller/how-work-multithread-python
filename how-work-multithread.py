import threading
import time

global var

var = False

def execute(msg):
  for i in range(5):
    if var:
      break
    print(i, msg)
    time.sleep(1)

print('init')

threading.Thread(target=execute, args=('runtime',)).start()

time.sleep(2)

print(' end')

var = True
