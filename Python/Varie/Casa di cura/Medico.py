from threading import Thread
from time import sleep
from CasaDiCura import CasaDiCura
from random import randint

class Medico(Thread):
	def __init__(self, nome, casa:CasaDiCura):
		super().__init__()
		self.nome = nome
		self.casa = casa
	
	def run(self):
		while True:
			print(f"{self.nome} cerca un paziente per operare")
			paziente = self.casa.chiamaPerOperazione()
			self.opera()
			print(f"{self.nome} ha finito di operare {paziente}, ora riordina la sala")
			self.preparaSala()
	
	def opera(self):
		sleep(randint(2,5))
	
	def preparaSala(self):
		sleep(randint(5,8))