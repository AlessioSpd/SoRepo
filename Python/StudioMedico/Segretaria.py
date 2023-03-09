from threading import Thread
from random import *
from time import sleep

class Segreatria(Thread):
    def __init__(self, salaAttesa):
        super().__init__()
        self.salaAttesa = salaAttesa
    
    def run(self):
        while True:
            paziente = self.salaAttesa.getProssimoPaziente()
            
            sleep(random())

            medicina = random()

            if medicina > 0.66:
                paziente.ricetta.medicina = 'aulin'
            elif medicina > 0.33:
                paziente.ricetta.medicina = 'xanax'
            else:
                paziente.ricetta.medicina = 'oki'
            
            paziente.ricetta.ricettaPronta()