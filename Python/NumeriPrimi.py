import math, time, multiprocessing
from threading import Thread, Lock, Condition

class Barrier:
    def __init__(self, n):
        self.soglia = n
        self.threadArrivati = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def wait(self):
        with self.lock:
            self.threadArrivati += 1
            print(f"Thread arrivati e stato incrementato  a {self.threadArrivati}")
            if self.threadArrivati == self.soglia:
                self.condition.notify_all()
            
            while self.threadArrivati < self.soglia:
                self.condition.wait()


def eprimo(n :int) -> bool:
    if n <=3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1),2):
        if n % i == 0:
            return False
    return True

def contaPrimiSeq(min :int, max :int) -> int:
    totale = 0
    for i in range(min, max+1):
        if (eprimo(i)):
            totale += 1
    return totale

class Macinatore(Thread):
    def __init__(self, min, max, b):
        Thread.__init__(self)
        self.min = min
        self.max = max
        self.totale = 0
        self.barrier = b

    def getTotale(self):
        return self.totale
    
    def run(self):
        self.totale = contaPrimiSeq(self.min, self.max)
        self.barrier.wait()

def contaPrimiMultiThread(min, max):
    if max < min:
        return 0
    
    threadReali = multiprocessing.cpu_count()
    # threadReali = 1
    fettina = (max - min + 1) // threadReali

    ciucci = []
    b = Barrier(threadReali + 1)

    for i in range(threadReali - 1):
        minI = min + i * fettina
        maxI = minI + fettina - 1
        ciucci.append(Macinatore(minI, maxI, b))
        ciucci[i].start()

    minI = min + (threadReali - 1) * fettina
    maxI = max
    ciucci.append(Macinatore(minI, maxI, b))
    ciucci[threadReali - 1].start()

    b.wait()

    totale = 0
    for i in range(threadReali):
        totale += ciucci[i].getTotale()
    return totale

start = time.time()
minimo = 100000
massimo = 1000000
print(f"Primi tra {minimo} e {massimo} : {contaPrimiMultiThread(minimo, massimo)}")
elapsed = time.time() - start
print(f"Tempo: {elapsed}")