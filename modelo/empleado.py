# from datetime import datetime


    # def __init__(self, username, email="", password="", create_time=datetime.now()):
class Empleado():
    def __init__(self,runEmpleado,nombreEmpleado,apellidoEmpleado,cargo,direccionEmpleado,claveEmpleado,correoEmpleado,comuna):
        self.__runEmpleado = runEmpleado
        self.__nombreEmpleado = nombreEmpleado 
        self.__apellidoEmpleado = apellidoEmpleado
        self.__cargo = cargo
        self.__direccionEmpleado = direccionEmpleado
        self.__claveEmpleado = claveEmpleado
        self.__correoEmpleado = correoEmpleado
        self.__comuna = comuna

        