from CasaDiCura import CasaDiCura
from Medico import Medico
from CreaPazienti import CreaPazienti

cs = CasaDiCura(3)
posca = Medico('Posca', cs)
generatore = CreaPazienti(cs)

posca.start()
generatore.start()