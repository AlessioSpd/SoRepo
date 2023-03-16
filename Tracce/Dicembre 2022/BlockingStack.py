from threading import RLock,Condition, Thread
import random
import time

class BlockingStack:
    
    def __init__(self,size):
        self.size = size
        self.elementi = []
        self.lock = RLock()
        self.conditionTuttoPieno = Condition(self.lock)
        self.conditionTuttoVuoto = Condition(self.lock)

        # Si poteva fare anche usando le condition già fornite
        # ma preferisco farlo così perché è più intuitivo
        self.conditionPutN = Condition(self.lock)

        self.FIFOmode = False
        
    def __find(self,t):
        try:
            if self.elementi.index(t) >= 0:
                return True
        except(ValueError):
            return False
    
    def put(self,t):
        self.lock.acquire()
        while len(self.elementi) == self.size:
            self.conditionTuttoPieno.wait()
        self.conditionTuttoVuoto.notify_all()
        self.elementi.append(t)
        self.lock.release()
    
    """def flush(self):
        with self.lock:
            self.elementi.clear()"""

    def flush(self):
        with self.lock:
            if len(self.elementi) == 0:
                return
            self.elementi.clear()
            self.conditionTuttoPieno.notify_all()

    def putN(self, L: list):
        with self.lock:
            if len(L) > len(self.elementi):
                return

            while (self.size - len(self.elementi)) < len(L):
                self.conditionPutN.wait()

            for e in L:
                self.put(e)

    def setFifo(self, onOff : bool):
        with self.lock:
            if self.FIFOmode != onOff:
                self.FIFOmode = onOff
    
    def take(self,t=None):
        self.lock.acquire()
        try:
            if t == None:
                while len(self.elementi) == 0:
                    self.conditionTuttoVuoto.wait()
                
                if len(self.elementi) == self.size:
                    self.conditionTuttoPieno.notify()
                    
                self.conditionPutN.notify_all()
                if self.FIFOmode:
                    return self.elementi.pop(0)
                else:
                    return self.elementi.pop()
            else:
                while not self.__find(t):
                    self.conditionTuttoVuoto.wait()
                if len(self.elementi) == self.size:
                    self.conditionTuttoPieno.notify()
                self.elementi.remove(t)    
                self.conditionPutN.notify_all()
                return t    
        finally:
            self.lock.release()
    

class Consumer(Thread): 
    
    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(random.random()*2)
            print(f"Estratto elemento {self.queue.take()}")
            


class Producer(Thread):

    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self): 
        while True:
            time.sleep(random.random() * 2)
            self.queue.put(self.name)
            print(f"Inserito elemento da {self.name}")
            
#  Main
#
buffer = BlockingStack(10)

producers = [Producer(buffer) for x in range(5)]
consumers = [Consumer(buffer) for x in range(3)]

for p in producers:
    p.start()

for c in consumers:
    c.start()