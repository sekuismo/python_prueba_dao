class Cargo:
    def __init__(self,listaCargos=[],identicaCargo="",descripcionCargo=""):
        self.__listaCargos = listaCargos
        self.__identicaCargo = identicaCargo
        self.__descripcionCargo = descripcionCargo

    def __str__(self):
        return f'Número de cargo: {self.__identicaCargo} \n Cargo:{self.__descripcionCargo}  '
    
    def setIdenticaCargo(self,num_cargo):
        self.__identicaCargo = num_cargo
    def getIndenticaCargo(self):
        return self.__identicaCargo
    def setDescripcionCargo(self,nom_cargo):
        self.__identicaCargo = nom_cargo
    def getDescripcionCargo(self):
        return self.__descripcionCargo
    def setLista(self,elemento):
        self.__listaCargos.append(elemento)
    def getLista(self):
        return self.__listaCargos