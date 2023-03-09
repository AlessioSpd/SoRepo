from threading import Thread, Lock
from queue import Queue
from BlockingSet import BlockingSet
from Ordine import Ordine

class Pizzeria:

    bufferOrdine = Queue(5) # è una libreria gia' thread-safe
    bufferPizze = BlockingSet(5)
    
    def putOrdine(self, tipoPizza, quantita):
        ordine = Ordine(tipoPizza, quantita)
        self.bufferOrdine.put(ordine)
        return ordine

    def getOrdine(self):
        return self.bufferOrdine.get()

    def putPizze(self, ordine):
        self.bufferPizze.add(ordine)

    def getPizze(self, ordine):
        return self.bufferPizze.remove(ordine)