from modelo.empleado import Empleado
from dao.dao_empleado import daoEmpleado
from utils.encoder import Encoder

class EmpleadoDTO:



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

    def findEmpleadoByCargo(nombre_cargo):
        daoempleado = daoEmpleado()
        
        return daoempleado.findEmpleadoByCargo(nombre_cargo)
    

