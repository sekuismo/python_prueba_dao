from modelo.empleado import Empleado
from dao.dao_empleado import daoEmpleado
from utils.encoder import Encoder

class EmpleadoDTO:

    # def listarEmpleados(self):
    #     daoempleado = daoEmpleado()
    #     resultado = daoempleado.listarEmpleados()
    #     lista = []
    #     if resultado is not None: # No se como acceder a los objetos cargo y comuna desde el dao de empleado (desde la tabla)
    #         for u in resultado:
    #             empleado = Empleado(runEmpleado=u[0], nombreEmpleado=u[1], apellidoEmpleado=u[2], None, direccionEmpleado=u[3], claveEmpleado=u[4], correoEmpleado=u[5], None)
    #             lista.append(empleado)
    #     return lista



    def addEmpleado(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo): 
        daoempleado = daoEmpleado()
        resultado = daoempleado.addEmpleado(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo)
        return resultado

    def delEmpleado(run):
        daoempleado = daoEmpleado()
        return daoempleado.delEmpleado(run)
        

    def updateEmpleado(nombre,apellido,direccion,idCargo,idComuna,run):
        daoempleado = daoEmpleado()
        return daoempleado.updateEmpleado(nombre,apellido,direccion,idCargo,idComuna,run)

    def findEmpleadoByComuna(comuna):
        daoempleado = daoEmpleado()
        return daoempleado.findEmpleadoByComuna(comuna)

        
    

