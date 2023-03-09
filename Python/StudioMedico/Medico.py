from threading import Thread
from random import *
from time import sleep

class Medico(Thread):
    def __init__(self, salaAttesa):
        super().__init__()
        self.salaAttesa = salaAttesa
    
    def run(self):
        while True:
            paziente = self.salaAttesa.getPazienteVisita()
            sleep(random())

            # genera un numero casuale tra 0 e 1
            prescrizione = random()

            if prescrizione > 0.66:
                paziente.ricetta.medicina = 'a casa'
                paziente.ricetta.ricettaPronta()
            elif prescrizione > 0.33:
                paziente.ricetta.medicina = 'stai bene'
            else:
                self.salaAttesa.putPazienteRicettaPrioritaria(paziente)
                paziente.ricetta.attendiEsito()