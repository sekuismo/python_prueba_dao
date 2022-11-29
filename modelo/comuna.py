class Comuna:
    def __init__(self,listaComuna=[],identificaComuna=0,descripcionComuna=""):
        self.__listaComuna = listaComuna
        self.__identificaComuna = identificaComuna
        self.__descripcionComuna = descripcionComuna

    def __str__(self):
        return f'ID Comuna :{self.__identificaComuna} \n  Comuna: {self.__descripcionComuna}'


    def setIdentificaComuna(self,id):
        self.__identificaComuna = id
    def getIdentificaComuna(self):
        return self.__identificaComuna
    def SetdescripcionComuna(self,comuna):
        self.__descripcionComuna = comuna
    def getDescripcionComuna(self):
        return self.__descripcionComuna   

    def setListaComuna(self,comuna):
        self.__listaComuna.append(comuna)
    def getListaComuna(self):
        return self.__listaComuna     