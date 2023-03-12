from threading import Thread,RLock,Condition
from random import randint

debug = True
deepDebug = False
def dprint(s):
    if deepDebug:
        print(s)

class RoundRobinLock:
    def __init__(self,N : int):
        self.nturni = N
        self.lock = RLock()
        self.conditions = [Condition(self.lock) for _ in range(0,N)]
        self.inAttesa = [0 for _ in range(0,N)]
        self.turnoCorrente = 0
        self.possessori = 0
   # Verifica che tra self.turnoCorrente e id non ci sia nessun thread in attesa con idTurno tale che
   # self.turnoCorrente < idTurno < id
   #
    def _possoPrendereMicrofono(self,id):
        if id == self.turnoCorrente:
            return True
        for i in range(1,self.nturni-1):
            idTurno = (id - i) % self.nturni
            if idTurno == self.turnoCorrente:
                return True
            if self.inAttesa[idTurno] > 0:
                return False


    def acquire(self,id : int):
        with self.lock:
            self.inAttesa[id] += 1
            while( self.possessori > 0 and self.turnoCorrente != id or
                self.possessori == 0 and not self._possoPrendereMicrofono(id)):
                dprint(f"Waiting {id}")
                self.conditions[id].wait()
                dprint(f"Waking {id} - Turno {self.turnoCorrente}")
# Se mi trovo in questo punto del codice, ho la garanzia che self.possessori == 0 e nessun thread di
# altro id ha bisogno del turno
# dunque prendo il turno
#
            dprint(f"Getting Lock {id}")
            self.turnoCorrente = id
            self.inAttesa[id] -= 1
            self.possessori += 1
            if debug:
                self.__print__()


    def release(self, id : int):
        with self.lock:
            self.possessori -= 1
            if self.possessori == 0:
                for i in range(1,self.nturni):
                    turno = (id + i) % self.nturni
                    if self.inAttesa[turno] > 0:
                        self.turnoCorrente = turno
                        self.conditions[turno].notifyAll()
                        dprint(f"Notifying {turno}")
                        break
            if debug:
                self.__print__()
                
    def __print__(self):
        with self.lock:
            print("=" * self.turnoCorrente + "|@@|" + "=" * (self.nturni - self.turnoCorrente -1) )
            for l in range(0,max(max(self.inAttesa),self.possessori)):
                o = ''
                for t in range(0,self.nturni):
                    if self.turnoCorrente == t:
                        if self.possessori > l:
                            o = o + "|o"
                        else:
                            o = o + "|-"
                    if self.inAttesa[t] > l:
                            o = o + "*"
                    else:
                        o = o + "-"
                    if self.turnoCorrente == t:
                        o = o + "|"
                print (o)
            print("")


class RoundRobinLockStarvationMitigation(RoundRobinLock):
    SOGLIASTARVATION = 5
    def __init__(self,N : int):
        super().__init__(N)
        self.consecutiveOwners = 0
    
    def acquire(self,id : int):
          with self.lock:
              self.inAttesa[id] += 1
              while( self.possessori > 0 and self.turnoCorrente != id
                     or
                     self.possessori == 0 and not self._possoPrendereMicrofono(id)
                     or
                     self.turnoCorrente == id and self.consecutiveOwners > self.SOGLIASTARVATION and
                     max(self.inAttesa) > 0
              ):
                  self.conditions[id].wait()

              self.turnoCorrente = id
              self.inAttesa[id] -= 1
              self.possessori += 1
              self.consecutiveOwners += 1
              if debug:
                  self.__print__()


    def release(self,id : int):
          with self.lock:
              self.possessori -= 1
              if self.possessori == 0:
                  for i in range(1,self.nturni):
                      turno = (id + i) % self.nturni
                      if self.inAttesa[turno] > 0:
                          self.turnoCorrente = turno
                          self.consecutiveOwners = 0
                          self.conditions[turno].notifyAll()
                          break


class RoundRobinLockConCoda(RoundRobinLock):

      def __init__(self,N : int):
          pass

      def acquire(self,id : int):
          pass

      def release(self,id : int):
          pass


class Animale(Thread):

      def __init__(self,id: int, idTurno : int, R : RoundRobinLock):
          super().__init__()
          self.idTurno = idTurno
          self.iterazioni = 10
          self.lock = R

      def run(self):
          while(self.iterazioni > 0):
                  self.iterazioni -= 1
                  self.lock.acquire(self.idTurno)
                  self.lock.__print__()
                  self.lock.release(self.idTurno)

NGruppi = 10
R = RoundRobinLockStarvationMitigation(NGruppi)
#R = RoundRobinLock(NGruppi)
for i in range(0,60):
    Animale(i,randint(0,NGruppi-1),R).start()
