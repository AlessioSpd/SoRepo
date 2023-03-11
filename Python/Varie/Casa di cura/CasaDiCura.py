from threading import Thread, Condition, Lock
from time import sleep
from queue import Queue
from random import randint

class CasaDiCura:
	def __init__(self, numPosti):
		self.numPosti = numPosti
		self.sala_preparazione = Queue(numPosti)
		self.lock = Lock()
		self.sala_preparatoria_piena = Condition(self.lock)
		self.sala_preparatoria_vuota = Condition(self.lock)
	
	def chiamaPerOperazione(self):
		with self.lock:
			while not len(self.sala_preparazione.queue) > 0:
				self.sala_preparatoria_vuota.wait()
			
			if len(self.sala_preparazione.queue) > 0:
				pazienteChiamato = self.sala_preparazione.get()
				print(f"Il medico ha preso {pazienteChiamato} per operare")
				self.sala_preparatoria_piena.notify_all()
				return pazienteChiamato			
	
	def entraPaziente(self, paziente: str):
		with self.lock:
			while not self.possoEntrareInPrep():
				self.sala_preparatoria_piena.wait()
				
			if self.possoEntrareInPrep():
				self.sala_preparazione.put(paziente)
				self.sala_preparatoria_vuota.notify()
				print(f"{paziente} è entrato nella sala preparazione", flush=True)
	
	def possoEntrareInPrep(self):
		return len(self.sala_preparazione.queue) < self.numPosti