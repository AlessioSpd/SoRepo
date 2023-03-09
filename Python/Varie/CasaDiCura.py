from threading import Thread, Condition, Lock
from time import sleep
from queue import Queue
from random import randint

class CasaDiCura:
	def __init__(self, numPosti):
		self.numPosti = numPosti
		self.sala_preparazione = Queue(numPosti)
		self.sala_operazione_occupata = False
		self.lock = Lock()
		self.paziente_sotto_ferri = ""
		self.sala_preparatoria_piena = Condition(self.lock)
	
	def chiamaPerOperazione(self):
		pass
	
	def operazioneFinita(self):
		pass
	
	def entraPaziente(self):
	    while self.possoEntrareInPrep():
		    pass
            
		#altrimenti si mette in attesa
		#se entra, esce dalla funzione
		
	
    def possoEntrareInPrep(self):
        pass
	
	def esciPaziente(self):
		pass

class Medico(Thread):
	def __init__(self, nome, casa:CasaDiCura):
		super().__init__()
		self.nome = nome
		self.casa = casa
	
	def run(self):
		print(f"{self.nome} cerca un paziente per operare")
		paziente = self.casa.chiamaPerOperazione()
		print(f"{self.nome} ha chiamato {paziente.nome} per operare")
		self.opera()
		print(f"{self.nome} ha finito di operare {paziente.nome}, ora riordina la sala")
		self.casa.operazioneFinita()
		self.preparaSala()
	
	def opera(self):
		sleep(2,5)
	
	def preparaSala(self):
		sleep(5,8)
	
class CreaPazienti(Thread):
	def __init__(self, casa):
		super().__init__()
		self.casa = casa
	
	def run(self):
		i = 0
		while True:
			self.casa.entraPaziente(f"Paziente_{i}")
			print(f"Paziente_{i} e entrato")
			i += 1
			sleep(2)