class Cargo:
    def __init__(self,listaCargos,identicaCargo,descripcionCargo):
        self.__listaCargos = listaCargos
        self.__identicaCargo = identicaCargo
        self.__descripcionCargo = descripcionCargo

    def __str__(self):
        return f' Número de cargo: {self.__identicaCargo} \n Cargo:{self.__descripcionCargo}  '
        