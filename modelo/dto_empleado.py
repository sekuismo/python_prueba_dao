from modelo.empleado import Empleado
from dao.dao_empleado import daoEmpleado
from utils.encoder import Encoder

class EmpleadoDTO:

    def listarEmpleados(self):
        daoempleado = daoEmpleado()
        resultado = daoempleado.listarEmpleados()
        lista = []
        if resultado is not None: # No se como acceder a los objetos cargo y comuna desde el dao de empleado (desde la tabla)
            for u in resultado:
                empleado = Empleado(runEmpleado=u[0], nombreEmpleado=u[1], apellidoEmpleado=u[2], None, direccionEmpleado=u[3], claveEmpleado=u[4], correoEmpleado=u[5], None)
                lista.append(empleado)
        return lista

    def buscarEmpleado(self, run):
        daoempleado = daoEmpleado()
        resultado = daoempleado.buscarEmpleado(Empleado(runEmpleado=run))
        return Empleado(resultado[0], resultado[1], resultado[2], None, resultado[3], resultado[4], resultado[5], None) if resultado is not None else None

    def validarLogin(self, run, clave):
        daouser = daoEmpleado()
        resultado = daoEmpleado.validarLogin(Empleado(runEmpleado=run, claveEmpleado=Encoder().encode(clave)))
        return Empleado(resultado[0]) if resultado is not None else None

    def actualizarEmpleado(self, nombre, apellido, direccion, clave, correo):
        daoempleado = daoEmpleado()
        resultado = daoempleado.actualizarEmpleado(Empleado(nombreEmpleado=nombre, apellidoEmpleado=apellido, direccionEmpleado=direccion, claveEmpleado=Encoder().encode(clave), correoEmpleado=correo))
        return resultado

    def agregarEmpleado(self, run, nombre, apellido, cargoN, direccion, clave, correo, comunaN): # No se como hacerle con los IDs
        daoempleado = daoEmpleado()
        resultado = daoempleado.agregarEmpleado(Empleado(runEmpleado=run, nombreEmpleado=nombre, apellidoEmpleado=apellido, cargo=cargoN, direccionEmpleado=direccion, claveEmpleado=Encoder().encode(clave), correoEmpleado=correo, comuna=comunaN))
        return resultado
    
    def eliminarEmpleado(self, run):
        daoempleado = daoEmpleado()
        resultado = daoempleado.eliminarEmpleado(Empleado(runEmpleado=run))
        return resultado
