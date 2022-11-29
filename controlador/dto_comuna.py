from modelo.comuna import Comuna
from dao.dao_comuna import DaoComuna


class ComunaDTO:

    def listarComuna(self):
        daocomuna = DaoComuna()
        resultado = daocomuna.listarComuna()
        comuna = Comuna()
        lista = []
        
        for element in resultado:
            comuna.setIdentificaComuna(element[1])
            comuna.SetdescripcionComuna(element[2])
            comuna.setListaComuna(comuna)
            print(f'Número de comuna: {element[1]}')
            print(f'Comuna: {element[2]}')
            # return comuna.getListaComuna()
                
    
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
    def delComuna(self,num_comuna):
        daocomuna = DaoComuna()
        daocomuna.delComuna(num_comuna)

    
