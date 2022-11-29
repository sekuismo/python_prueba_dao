from modelo.comuna import Comuna
from dao.dao_comuna import DaoComuna
from utils.encoder import Encoder

class ComunaDTO:

    def listarComuna():
        daocomuna = DaoComuna()
        resultado = daocomuna.listarComuna()
        lista = []
        if resultado is not None:
            for u in resultado:
                Comuna = Comuna(codigoComuna=u[0], nombreComuna=u[1], descripComuna=u[2])
                lista.append(Comuna)
        return lista
    
    def buscarComuna(self,numero_comuna):
        daocomuna = DaoComuna()
        resultado = daocomuna.buscarComuna(numero_comuna)
        return resultado

    def modificarComuna(nombre_comuna,numero_comuna):
        daocomuna = DaoComuna()
        resultado = daocomuna.modificarComuna(nombre_comuna,numero_comuna)
        return resultado

    def agregarComuna(numeroComuna,nombreComuna):
        daocomuna = DaoComuna()
        resultado = daocomuna.agregarComuna(numeroComuna,nombreComuna)
        return resultado

    
