from modelo.cargo import Cargo
from dao.dao_cargo import DaoCargo
from utils.encoder import Encoder

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





# def buscarUsuario(self, username):
#         daouser = daoUser()
#         resultado = daouser.buscarUsuario(User(username=username))
#         return User(resultado[0], resultado[1], resultado[2]) if resultado is not None else None

#     def validarLogin(self, username, clave):
#         daouser = daoUser()
#         resultado = daouser.validarLogin(User(username=username, password=Encoder().encode(clave)))
#         return User(resultado[0]) if resultado is not None else None
#     def actualizarUsuario(self, username, email, password):
#         daouser = daoUser()
#         resultado = daouser.actualizarUsuario(User(username=username, email=email, password=Encoder().encode(password)))
#         return resultado
#     def agregarUsuario(self, username, email, password):
#         daouser = daoUser()
#         resultado = daouser.agregarUsuario(User(username=username, email=email, create_time= datetime.now(), password=Encoder().encode(password)))
#         return resultado

        
    

