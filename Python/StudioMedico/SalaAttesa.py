from queue import Queue
from threading import RLock, Condition

class SalaAttesa:
    coda_visita                 = Queue()
    coda_ricetta                = Queue()
    coda_ricetta_prioritaria    = Queue()
    lockSegretaria = RLock()
    conditionNessunaRicetta = Condition(lockSegretaria)


    def putPazienteVisita(self, paziente):
        self.coda_visita.put(paziente)
        paziente.ricetta.attendiEsito()
        return paziente.ricetta

    def getPazienteVisita(self):
        return self.coda_visita.get()

    def putPazienteRicetta(self, paziente):
        self.coda_ricetta.put(paziente)

        with self.lockSegretaria:
            self.conditionNessunaRicetta.notify_all()

        paziente.ricetta.attendiEsito()
        return paziente.ricetta
    
    def putPazienteRicettaPrioritaria(self, paziente):
        self.coda_ricetta_prioritaria.put(paziente)
        
        with self.lockSegretaria:
            self.conditionNessunaRicetta.notify_all()

        paziente.ricetta.attendiEsito()
        return paziente.ricetta

    def getProssimoPaziente(self):
        self.lockSegretaria.acquire()
        try:
            while self.coda_ricetta.empty() and self.coda_ricetta_prioritaria.empty():
                self.conditionNessunaRicetta.wait()
            
            if not self.coda_ricetta_prioritaria.empty():
                return self.coda_ricetta_prioritaria.get()
            
            return self.coda_ricetta.get()
        finally:
            self.lockSegretaria.release()

