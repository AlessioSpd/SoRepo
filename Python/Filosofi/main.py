from threading import Thread, Lock, Condition
from time import sleep
from random import randrange

class Bacchetta:
    def __init__(self):
        self.lock = Lock()
        self.occupata = False

    def checkOccupata(self):
        return self.occupata

    def prendiBacchetta(self):
        # self.lock.acquire()
        self.occupata = True
    
    def lasciaBacchetta(self):
        # self.lock.release()
        self.occupata = False
    
class Tavolo:
    def __init__(self):
        self.bacchetta = [Bacchetta() for _ in range(5)]
        self.lock = Lock()
        self.cond = Condition(self.lock)

    def prendiLockSimultaneo(self, posizione):
        while self.bacchetta[posizione].checkOccupata() or self.bacchetta[(posizione+1) % 5].checkOccupata():
            self.cond.wait()
        
        self.bacchetta[posizione].prendiBacchetta()
        self.bacchetta[(posizione+1) % 5].prendiBacchetta()

    def mollaLockSimultaneo(self, posizione):
        with self.lock:
            self.bacchetta[posizione].lasciaBacchetta()
            self.bacchetta[(posizione+1) % 5].lasciaBacchetta()
            self.cond.notifyAll()

class Filosofo(Thread):
    def __init__(self, tavolo, pos):
        super().__init__()
        self.posizione = pos
        self.tavolo = tavolo
        self.name = "Philip %s" % str(pos)

    def attesaCasuale(self, msec):
        sleep(randrange(msec)/1000.0)
        # sleep(msec/1000.0)

    def pensa(self):
        print(f"Il filosofo {self.name} pensa.")
        # self.attesaCasuale(2000)
        print(f"Il filosofo {self.name} smette di pensare.")

    def mangia(self):
        
        print(f"Il filosofo {self.name} vuole mangiare.")
        
        self.tavolo.prendiLockSimultaneo(self.posizione)
        print(f"Il filosofo {self.name} ha le sue bacchette e mangia.")
        
        self.attesaCasuale(1)
        
        self.tavolo.mollaLockSimultaneo(self.posizione)
        print(f"Il filosofo {self.name} mnolla le sue bacchette.")

        print(f"Il filosofo {self.name} termina di mangiare.")

    def run(self):
        while True:
            self.pensa()
            self.mangia()

tavolo = Tavolo()

filosofi = [Filosofo(tavolo, i) for i in range(5)]

for f in filosofi:
    f.start()