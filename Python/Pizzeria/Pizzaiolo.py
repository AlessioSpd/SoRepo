from threading import Thread
from random import randint, random, randrange
from time import sleep

class Pizzaiolo(Thread):
    def __init__(self, name, pizzeria):
        super().__init__()
        super().setName(name)
        self.pizzeria = pizzeria
    
    def run(self):
        while True:
            # step 1 -> prende una comanda (ordine)
            ordine = self.pizzeria.getOrdine()
            print('Il pizzaiolo %s ha prelevato l ordine con id %d' % (self.name, ordine.id))
            
            # step 2 -> inizia preparazione (proporzionale al numero delle pizze)
            seconds = random()
            sleep(seconds * ordine.quantita)
            ordine.prepara()
            print('Il pizzaiolo %s ha preparato l ordine con id %d, %d pizze di tipo %d' % (self.name, ordine.id, ordine.quantita, ordine.tipoPizza))

            # step 3 -> inserire l'ordine pronto nel buffer delle pizze
            self.pizzeria.putPizze(ordine)

            # step 4 -> il pizzaiolo riposa
            sleep(randint(1,3))