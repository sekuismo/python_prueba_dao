from modelo.comuna import Comuna
from dao.dao_comuna import daoComuna
from utils.encoder import Encoder

class ComunaDTO:

    def listarComuna(self):
        daocomuna = daoComuna()
        resultado = daoComuna.listarComuna()
        lista = []
        if resultado is not None:
            for u in resultado:
                Comuna = Comuna(codigoComuna=u[0], nombreComuna=u[1], descripComuna=u[2])
                lista.append(Comuna)
        return lista
    
    def buscarComuna(self, codigoComuna):
        daocomuna = daoComuna()
        resultado = daoComuna.buscarComuna(Comuna(codigoComuna=codigoComuna))
        return Comuna(resultado[0], resultado[1], resultado[2]) if resultado is not None else None

    def modificarComuna(self, codigoComuna, nombreComuna, descripComuna):
        daocomuna = daoComuna()
        resultado = daoComuna.modificarComuna(Comuna(codigoComuna=codigoComuna, nombreComuna=nombreComuna, descripComuna=descripComuna))
        return resultado

    def agregarComuna(self, codigoComuna, nombreComuna, descripComuna):
        daocomuna = daoComuna()
        resultado = daoComuna.agregarComuna(Comuna(codigoComuna=codigoComuna, nombreComuna=nombreComuna, descripComuna=descripComuna))
        return resultado

    
