from threading import Thread
from random import randint, random, randrange
from time import sleep

class Cliente(Thread):
    def __init__(self, name, pizzeria):
        super().__init__()
        super().setName(name)
        self.pizzeria = pizzeria
    
    def run(self):
        while True:
            # step 1 -> genera un ordine
            tipoPizza = randint(1,4)
            quantita = randint(1,6)
        
            # step 2 -> l'ordine viene inserito nel buffer ordini
            ordine = self.pizzeria.putOrdine(tipoPizza, quantita)
            print('Il cliente %s ha inserito l ordine con id %d' % (self.name, ordine.id))

            # step 3 -> il cliente entra in attesa non bloccante (sleep)
            sleep(randint(1,4) * quantita)

            # step 4 -> il cliente controlla se il suo ordine e' pronto
                    # se non lo e', il cliente netra in attesa bloccante\
            
            self.pizzeria.getPizze(ordine)

            # step 5 -> il cliente mangia la pizza e po va via
            sleep(randint(1,5))