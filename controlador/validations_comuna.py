from controlador.dto_comuna import ComunaDTO
def listAll():
    print("Listado de Comunas")
    resultado = ComunaDTO().listarComuna()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindComuna():
    codigoComuna = int(input("Ingrese el codigo de la comuna a buscar : "))
    if codigoComuna < 0:
        print("Codigo de comuna incorrecto")
        return validateFindComuna()
    else:
        resu = ComunaDTO().buscarComuna(codigoComuna)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Comuna No encontrada")

def validateUpdateComuna():
    codigoComuna = int(input("Ingrese el nombre de usuario a modificar : "))
    if codigoComuna < 0:
        print("Debe ingresar un codigo de comuna valido")
        return validateUpdateComuna()
    resu = ComunaDTO().buscarComuna(codigoComuna)
    if resu is not None:
        print("Datos --> ", resu)
        codigoComuna = int(input("Ingrese codigo de la comuna : ")) 
        nombreComuna = input("Ingrese nombre de la comuna : ") 
        descripComuna = input("Ingrese descripcion de la comuna")
        print(ComunaDTO().actualizarComuna(codigoComuna, nombreComuna, descripComuna))

    else:
        print("Usuario No encontrado")

def validateAddComuna():
    codigocomuna = int(input("Ingrese nombre de usuario a incorporar: "))
    if codigocomuna < 0:
        print("Debe ingresar un codigo valido para la comuna")
        return validateAddComuna()
    resu = ComunaDTO().buscarComuna(codigocomuna)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:
        nombreComuna = input("Ingrese nombre de comuna : ") 
        descripComuna = input("Ingrese descripcion de comuna : ") 
        print(ComunaDTO().agregarComuna(codigocomuna, nombreComuna,descripComuna))

def validarLogin():
    username = input("Ingrese nombre de usuario : ")
    clave = input("Ingrese contraseña : ")
    resultado = ComunaDTO().validarLogin(username, clave)
    return resultado
