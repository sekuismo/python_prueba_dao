from controlador.dto_cargo import CargoDTO

#Módulo de validaciones de los cargos 


def validarFindUser():
    numero_cargo = input('ingrese el número de cargo a buscar')
    try:
        numero_cargo = int(numero_cargo)
        resultado = CargoDTO.findCargo(numero_cargo)
        print(resultado)
    except:
        print('Solo ingrese números , no letras !!!')
        validarFindUser()
 

def validarAddCargo():
    num_cargo = input('ingrese el número del cargo')
    nombre_cargo = input ('ingrese el nombre del cargo')
    try:
        num_cargo = int(num_cargo)
        resultado =CargoDTO.addCargo(num_cargo,nombre_cargo)
        print(resultado)

    except:
        print('EL CARGO SE INGRESA CON UN NÚMERO'.center(30,'-'))

        

def validarUpdateCargo():

        try:
            num_cargo = input('ingrese el número del cargo a modificar')
            num_cargo = int(num_cargo)
            nombre_cargo = input ('ingrese el nuevo  nombre del cargo') 
            resultado = CargoDTO.updateCargo(num_cargo,nombre_cargo)
            print(resultado)
        except:
            print('algo falló en la actualización')

def validarDelCargo():
    try:
        num_cargo = input('ingrese el número del cargo a eliminar')
        num_cargo = int(num_cargo)
        resultado = CargoDTO.delCargo(num_cargo)
        print(resultado)
        

    except:
        print('no funcionó bien :(')

def validarMostrarCargos():
    cargodto = CargoDTO
    cargodto.findAllCargos()

