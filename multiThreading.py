from threading import *
from time import *


class A(Thread):
    def run(self):
        for i in range(5):
            print("Hi!")
            sleep(1)    # Here sleep will stop execution of t1 for 1sec. and t2 will execute then.


class B(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1)


t1 = A()
t2 = B()
t1.start()
sleep(0.1)  # Here sleep will stop execution of t1 and run t2.
t2.start()
t1.join()   # Here join will make both t1 and t2 to continue until it finished its process then it will print Bye!
t1.join()
print("Bye!")
