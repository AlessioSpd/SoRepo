from threading import Thread, Lock, Condition
from time import sleep
from queue import Queue

class Ponte:
    def __init__(self):
        self.occupato = False
        self.tipo_occupato = -1
        self.lock = Lock()
        self.ponte_occupato = Condition(self.lock)
        self.turisti_sul_ponte = 0
    
    def occupa(self, tipo):
        with self.lock:
            while not self.possoPassare(tipo):
                self.ponte_occupato.wait()
            
            if self.possoPassare(tipo):
                self.occupato = True
                self.tipo_occupato = tipo



    def possoPassare(self, tipo):
        if not self.occupato:
            return True
        elif self.occupato and tipo == self.tipo_occupato:
            return True
        
        return False

# mare = 0 | # montagna = 1
class Turista(Thread):
    def __init__(self, tipo, ponte:Ponte):
        super().__init__()
        self.tipo = tipo
        self.ponte = ponte
    
    def run(self):
        while True:
            self.ponte.occupa(self.tipo)
