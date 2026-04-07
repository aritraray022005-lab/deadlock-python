import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

# Deadlock 
def deadlock_example():

    def t1():
        print("T1: acquiring lock1")
        lock1.acquire()

        time.sleep(1)

        print("T1: waiting for lock2")
        lock2.acquire()

    def t2():
        print("T2: acquiring lock2")
        lock2.acquire()

        time.sleep(1)

        print("T2: waiting for lock1")
        lock1.acquire()

    threading.Thread(target=t1).start()
    threading.Thread(target=t2).start()


#  Fixed version with Resource Ordering 
def safe_example():

    def t(name):
        print(f"{name}: acquiring locks in order")

        lock1.acquire()
        lock2.acquire()

        print(f"{name}: done")

        lock2.release()
        lock1.release()

    threading.Thread(target=t, args=("T1",)).start()
    threading.Thread(target=t, args=("T2",)).start()



deadlock_example()
# safe_example()