from Paziente import Paziente
from Ricetta import Ricetta
from SalaAttesa import SalaAttesa
from Medico import Medico
from Segretaria import Segreatria
from GeneraPazienti import GeneraPazienti

def main():
    salaAttesa = SalaAttesa()
    medico = Medico(salaAttesa)
    segreataria_1 = Segreatria(salaAttesa)
    segreataria_2 = Segreatria(salaAttesa)

    generaPazienti = GeneraPazienti(salaAttesa)

    medico.start()
    segreataria_1.start()
    segreataria_2.start()
    
    generaPazienti.start()

if __name__ == '__main__':
    main()