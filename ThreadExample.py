

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


#create class object
t1 = Hello()
t2 = Hi()


#runs the thread
t1.start()
sleep(.2)
t2.start()


#wait for thread to join back in with main thread
t1.join()
t2.join()



print("Bye")
