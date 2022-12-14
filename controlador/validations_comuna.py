
from modelo.comuna import Comuna
from controlador.dto_comuna import ComunaDTO

#Módulo de validaciones de las comunas


def validateListarComunas():
    comunas = ComunaDTO()
    lista = comunas.listarComuna()



def validateFindComuna():
    numero_comuna = input("Ingrese el codigo de la comuna a buscar : ")
    if numero_comuna =="":
        print('NO PUEDE SER UN CAMPO VACÍO')
        validateFindComuna()
    else:
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
    if numero_comuna =="":
        print('NO PUEDE SER UN CAMPO VACÍO')
    else:
        nombre_comuna = input('ingrese el nuevo nombre de la comuna ')
        if nombre_comuna =="":
            print('NO PUEDE SER UN CAMPO VACÍO')
            validateUpdateComuna()
        else:
            try:
                numero_comuna = int(numero_comuna)
                resultado = ComunaDTO.modificarComuna(nombre_comuna,numero_comuna)
                print(resultado)

            except:
                print('algo salió mal ')

def validateAddComuna():
    codigocomuna = input("   ingrese el identificador de la comuna")
    if codigocomuna =="":
        print('NO PUEDE SER UN CAMPO VACÍO')
        validateAddComuna()
    else:
        nombreComuna = input("   ingrese el nombre de la comuna")
        if nombreComuna=="":
            print('NO PUEDE SER UN CAMPO VACÍO')
            validateAddComuna()
        else:
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

def validateDelComuna():
    num_comuna = input('ingrese el número de la comuna a eliminar')
    if num_comuna =="":
        print('NO PUEDE SER UN CAMPO VACÍO')
        validateDelComuna()
    else:
        try:
            num_comuna = int(num_comuna)
            dtoComuna = ComunaDTO()
            resultado = dtoComuna.delComuna(num_comuna)
            
        except:
            print('algo salió mal')
