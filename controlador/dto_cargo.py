from modelo.cargo import Cargo
from dao.dao_cargo import DaoCargo


#hay que escribir todos los métodos

#el dto no tiene init
class CargoDTO:
    def findCargo(numero_cargo):
        daoCargo = DaoCargo()
        resultado = daoCargo.findCargo(numero_cargo)
          
        if resultado is not None:
            return Cargo(resultado[0], resultado[1], resultado[2])
        else:
            return "no hay nada aquí"
    def addCargo(num_cargo,nombre_cargo):
        daocargo = DaoCargo()
        resultado = daocargo.addCargo(num_cargo,nombre_cargo)
        return resultado

    def updateCargo(num_cargo,nombre_cargo):
        daocargo = DaoCargo()
        resultado = daocargo.updateCargo(num_cargo,nombre_cargo)
        return resultado
    def delCargo(num_cargo):
        daocargo = DaoCargo()
        resultado = daocargo.delCargo(num_cargo)
        return resultado

    def findAllCargos():
        #se agregan los atributos de la base de datos a la clase correspondiente,
        #Se imprime cada uno de los cargos a partir del fetchAll() y un ciclo
        #solo se imprime  el identificador dado por el usuario y el nombre del cargo
        try:
            daocargo = DaoCargo()
            cargos = daocargo.findAllCargos()
            for element in cargos:
                cargo = Cargo()
                cargo.setIdenticaCargo(element[0])
                cargo.setDescripcionCargo(element[1])
                cargo.setLista(cargo)
                print(f'Identificador del cargo: {element[0]}')
                print(f'Nombre del cargo       : {element[1]}')

                
        except:
            print('no funka :(')




