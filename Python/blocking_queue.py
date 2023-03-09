from random import random
from threading import Thread, Lock, Condition
from time import sleep

class BlockingQueue2020:
    def __init__(self, dim):
        self.ins = 0
        self.out = 0 
        self.slotPieni = 0
        self.dim = dim
        self.theBuffer = [None] * dim
        self.lock = Lock()
        self.full_condition = Condition(self.lock)
        self.empty_condition = Condition(self.lock)

    def put(self, c):
        with self.lock:

            while self.slotPieni == len(self.theBuffer):
                self.full_condition.wait()

            if self.slotPieni == 0:
                self.empty_condition.notify()
            
            self.theBuffer[self.ins] = c
            self.ins = (self.ins + 1) % len(self.theBuffer)
            self.slotPieni += 1


    def get(self):
        with self.lock:
            while self.slotPieni == 0:
                self.empty_condition.wait()

            if self.slotPieni == len(self.theBuffer):
                self.full_condition.notify()

            returnValue = self.theBuffer[self.out]
            self.out = (self.out + 1) % len(self.theBuffer)
            self.slotPieni -= 1
            
            return returnValue
    
    def show(self):
        self.lock.acquire()
        val = [None] * self.dim

        for i in range(0, self.slotPieni):
            val[(self.out + i) % (len(self.theBuffer))] = '*'
        
        for i in range(0, len(self.theBuffer) - self.slotPieni):
            val[(self.ins + i) % (len(self.theBuffer))] = '-'

        print("In: %d Out: %d C: %d" % (self.ins, self.out, self.slotPieni))
        print("".join(val))
        self.lock.release()

class Consumer(Thread):
    def __init__(self, buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            sleep(random()*2)
            palluzza = self.queue.get()
            # print("Sono il thread %s e ho prelevato il valore %s" % (self.name, palluzza))
            self.queue.show()

class Producer(Thread):
    def __init__(self, buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
         while True:
            sleep(random()*2)
            palluzza = "palluzza:" + self.name
            # print("Sono il thread %s e ho inserito il valore %s" % (self.name, self.name))
            self.queue.put(palluzza)
            self.queue.show()


buffer = BlockingQueue2020(10)
producers = [Producer(buffer) for x in range(2)]
consumers = [Consumer(buffer) for x in range(5)]

for p in producers:
    p.start()

for c in consumers:
    c.start()