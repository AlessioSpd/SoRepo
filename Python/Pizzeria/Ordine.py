class Ordine:
    nextId = 0 #variabile statica

    def __init__(self, tipoPizza, quantita):
        self.tipoPizza = tipoPizza
        self.quantita = quantita
        self.id = Ordine.nextId
        Ordine.nextId += 1

        self.pizze = ""
    
    def prepara(self):
        for i in range(0, self.quantita):
            if self.tipoPizza == 1:
                tipo = "-"
            elif self.tipoPizza == 2:
                tipo = '+'
            elif self.tipoPizza == 3:
                tipo = '/'
            else:
                tipo = '*'

            self.pizze += "(" + tipo + ")"