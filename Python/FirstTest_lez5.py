from threading import Thread, Lock

class Stampa:

    def __init__(self):
         self.lock = Lock() 

    def stampaStriscia(self, c, l):
        self.lock.acquire()
        for i in range(0, l+1):
            print(c, end='', flush=True)
        print('')
        self.lock.release()

class StampaAsterischi(Thread):
    def __init__(self, s : Stampa):
        super().__init__()
        self.st = s
    
    def run(self):
        # while True:
            self.st.stampaStriscia('*', 15)

class StampaTrattini(Thread):
    def __init__(self, s : Stampa):
        super().__init__()
        self.st = s
    
    def run(self):
        # while True:
            self.st.stampaStriscia('-', 10)

s = Stampa()

jhon = StampaAsterischi(s)
al = StampaTrattini(s)

#se sostuissimo start con run non si starta il thread
# ma si chiama la funzione in modo sequenziale
# se lo fai all'esame, ti boccio
jhon.start() 
al.start()
