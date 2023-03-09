# Un casello autostradale è composto da N porte dove i veicoli pagano un
# pedaggio calcolato secondo una tariffa chilometrica T. Il casello include una
# variabile incasso che memorizza l’ammontare di denaro riscosso nella giornata
# attraverso tutte le porte.
# Ogni veicolo effettua una volta sola le seguenti operazioni:
# 1. percorre un tratto di autostrada di x chilometri (con x compreso tra 50 e
# 100), impiegando 40 secondi per ogni chilometro;
# 2. giunto al casello, sceglie a caso la porta p a cui accodarsi;
# 3. accede alla porta p, dopo aver atteso in ordine FIFO che i precedenti veicoli
# abbiano completato le operazioni di pagamento su quella porta;
# 4. impiega tra 3 e 6 secondi per effettuare il pagamento;
# 5. rilascia la porta p ed abbandona l’autostrada.
# Ad ogni pagamento, la variabile incasso del casello deve essere incrementata di
# una quantità pari a x * T.
# Si modellino in Java i veicoli attraverso dei Thread e si implementino due
# soluzioni che riproducano il funzionamento del problema sopra descritto
# utilizzando:
# 1. la classe Semaphore del package java.util.concurrent
# 2. gli strumenti di mutua esclusione e sincronizzazione del package
# java.util.concurrent.locks.
# Si scriva infine un main d'esempio che faccia uso di una delle due soluzioni
# precedenti. A tal fine si inizializzi un certo numero V di veicoli, assegnando ad N
# ed a T dei valori a scelta dello studente.


from threading import Thread, Lock, Condition, Barrier
from random import randint
from time import sleep
from queue import Queue

class Casello:
    def __init__(self, entrate):
        self.entrate = entrate
        self.lista_entrate = []
        self.inizializzaCode(entrate)
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.somma = 0
        self.tariffa = 2

    def getEntrate(self):
        return self.entrate
    
    def inizializzaCode(self, entrate):
        for i in range(entrate):
            print(f"Lista {i} inizializzata")
            self.lista_entrate.append(Queue())
        
    def scegliEntrata(self, nomeThread, entrata):
        self.lista_entrate[entrata].put(nomeThread)
    
    def sonoPrimo(self, nome, entrata):
        if nome == self.lista_entrate[entrata].queue[0]:
            return True
        return False
    
    def paga(self, entrata, km):
        self.lista_entrate[entrata].get()
        self.somma += km * self.tariffa

    def getSomma(self):
        return self.somma


class Veicolo(Thread):
    def __init__(self, casello, name):
        super().__init__()
        self.casello = casello
        self.nome = name
        self.lock = Lock()
        self.aspettoChePago = Condition(self.lock)
    
    def run(self):
        self.chilometri = randint(5,10)
        sleep(self.chilometri * 2)
        self.portaSelezionata = randint(0,self.casello.getEntrate()-1)
        print(f"{self.nome}: scelgo la porta {self.portaSelezionata}")
        self.casello.scegliEntrata(self.name, self.portaSelezionata)
        print(f"{self.nome}: mi metto in attesa")
        while not self.casello.sonoPrimo(self.nome, self.portaSelezionata):
            self.aspettoChePago.wait()
        
        if self.casello.sonoPrimo(self.nome, self.portaSelezionata):
            print(f"{self.nome}: sono primo e pago")
            tempoPagamento = randint(1,2)
            self.casello.paga(self.portaSelezionata, self.chilometri)
            sleep(tempoPagamento)
            print(f"{self.nome}: ho finito e muoio")
            self.aspettoChePago.notify_all()



RomaSud = Casello(5)

for i in range(5):
    Veicolo(RomaSud, f"Auto_{i}").start()

barr = Barrier(6)
barr.wait()
print(RomaSud.getSomma())
