from threading import RLock, Condition
from random import *
from time import sleep

class Ricetta:
    lock = RLock()
    condition = Condition(lock)
    medicina = None

    def attendiEsito(self):
        self.lock.acquire()

        while self.medicina == None:
            self.condition.wait()
        
        self.lock.release()

    def ricettaPronta(self):
        self.lock.acquire()
        self.condition.notify_all()
        self.lock.release()
