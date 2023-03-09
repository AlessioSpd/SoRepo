from random import randint

class Striscia:
    size = 20

    def __init__(self):
        self.striscia = list()
        self.fine = False
        self.gatto = randint(0, self.size-1)
        self.topo = randint(0, self.size-1)
        self.direzione = 1
        
        for i in range(0, self.size):
            self.striscia.append('_')
        
        self.striscia[self.topo] = '.'
        self.striscia[self.gatto] = '*'
    
    def printStriscia(self):
        print("|%s|" % ''.join(self.striscia))
        return self.fine

    def muoviGatto(self):
        if self.fine: return self.fine

        self.striscia[self.gatto] = '_'
        self.gatto += self.direzione

        if self.gatto > self.size - 1 or self.gatto < 0:
            self.direzione = -self.direzione
            self.gatto += 2 * self.direzione
        
        self.striscia[self.gatto] = '*'

        if self.gatto == self.topo:
            self.fine = True
            self.striscia[self.gatto] = '@'
            return True
        return False
    
striscia = Striscia()
striscia.printStriscia()
striscia.muoviGatto()
striscia.printStriscia()
