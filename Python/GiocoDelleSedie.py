from random import random, randrange
from threading import Thread, Lock
from time import sleep

# classe di elemento condiviso dai thread
class Posto:
    def __init__(self):
        self.lock = Lock()
        self.occupato = False
    
    def libero(self):
        with self.lock:
            return not self.occupato
    
    def testaEdOccupa(self):
        with self.lock:
            if self.occupato:
                return False
            else:
                self.occupato = True
                return True

class Display(Thread):
    def __init__(self, posti):
        super().__init__()
        self.posti = posti
    
    def run(self):
        while True:
            sleep(1)
            for i in range(0, len(self.posti)):
                if self.posti[i].libero():
                    print('-', end='', flush=True)
                else:
                    print('o', end='', flush=True)
            print('')

class Partecipante(Thread):
    def __init__(self, posti):
        super().__init__()
        self.posti = posti
    
    def run(self):
        sleep(randrange(5))
        for i in range(0, len(posti)):
            if self.posti[i].testaEdOccupa():
                print("Sono il thread %s. Occupo il posto %d" % (self.name, i), flush=True)
                return
        print("Sono il thread %s. Ho perso" % (self.name), flush=True)

n_sedie = 10
posti = [Posto() for i in range(0, n_sedie)]

lg = Display(posti)
lg.start()

for i in range(0, n_sedie+1):
    t = Partecipante(posti)
    t.start()