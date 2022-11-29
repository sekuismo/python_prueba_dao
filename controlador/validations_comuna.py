#aquí van las validaciones de las comunas 
from modelo.comuna import Comuna
from controlador.dto_comuna import ComunaDTO

def validateListarComunas():
    comunas = ComunaDTO()
    lista = comunas.listarComuna()
    for element in lista:
        print(element.getIdentificaComuna())
        print(element.getDescripcionComuna())


def validateFindComuna():
    numero_comuna = input("Ingrese el codigo de la comuna a buscar : ")
    try:
        numero_comuna = int(numero_comuna)
        if numero_comuna < 0:
            print("Codigo de comuna incorrecto")
            return validateFindComuna()
        else:
            resu = ComunaDTO().buscarComuna(numero_comuna)
            if resu is not None:
                print(f"Resultado : {resu}")
            else:
                print("Comuna No encontrada")
    except:
        print('algo pasó')

def validateUpdateComuna():
    numero_comuna = input('ingrese el número de la comuna a modificar :')
    nombre_comuna = input('ingrese el nuevo nombre de la comuna ')
    try:
        numero_comuna = int(numero_comuna)
        resultado = ComunaDTO.modificarComuna(nombre_comuna,numero_comuna)
        print(resultado)

    except:
        print('algo salió mal ')

def validateAddComuna():
    codigocomuna = input("   ingrese el identificador de la comuna")
    nombreComuna = input("   ingrese el nombre de la comuna")
    try:
        codigocomuna = int(codigocomuna)
        
        resultado = ComunaDTO.agregarComuna(codigocomuna, nombreComuna,)
        print(resultado)
        print('exitoso!')
    except:
        print('paso algo ')

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    resultado = ComunaDTO().validarLogin(username, clave)
    return resultado
