import threading
import time

mutex = threading.Lock()

def count():
    global mutex
    mutex.acquire()
    print("1", end = '')
    time.sleep(0.001)
    print("2", end = '')
    time.sleep(0.001)
    print("3")
    mutex.release()


threads=[None] * 100
for i in range(0, 100):
    threads[i] = threading.Thread(target=count)

for i in range(0, 100):
    threads[i].start()
    
for i in range(0, 100):
    threads[i].join()
print("done")  