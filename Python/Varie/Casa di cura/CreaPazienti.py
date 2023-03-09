from threading import Thread
from time import sleep
from CasaDiCura import CasaDiCura

class CreaPazienti(Thread):
	def __init__(self, casa: CasaDiCura):
		super().__init__()
		self.casa = casa
	
	def run(self):
		i = 0
		while True:
			self.casa.entraPaziente(f"Paziente_{i}")
			i += 1
			sleep(2)