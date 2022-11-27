

from controlador.dto_cargo import CargoDTO

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

# def listAll():
#     print("Listado de Usuarios")
#     resultado = UserDTO().listarUsuarios()
#     if len(resultado) > 0:
#         for u in resultado:
#             print(u)
#     else:
#         print("no hay resultados")

# def validateFindUser():
#     username = input("Ingrese el nombre de usuario a buscar : ")
#     if username == "":
#         print("Nombre de usuario incorrecto")
#         return validateFindUser()
#     else:
#         resu = UserDTO().buscarUsuario(username)
#         if resu is not None:
#             print(f"Resultado : {resu}")
#         else:
#             print("Usuario No encontrado")
# def validateUpdateUser():
#     username = input("Ingrese el nombre de usuario a modificar : ")
#     if len(username) == 0:
#         print("Debe ingresar un nombre de usuario")
#         return validateUpdateUser()
#     resu = UserDTO().buscarUsuario(username)
#     if resu is not None:
#         print("Datos --> ", resu)
#         email = input("Ingrese email : ") #crear función para validar email
#         clave = input("Ingrese clave : ") #crear funci+on para valida clave
#         print(UserDTO().actualizarUsuario(username, email,clave))

#     else:
#         print("Usuario No encontrado")
# def validateAddUser():
#     username = input("Ingrese nombre de usuario a incorporar: ")
#     if len(username) == 0:
#         print("Debe ingresar un nombre de usuario")
#         return validateAddUser()
#     resu = UserDTO().buscarUsuario(username)
#     if resu is not None:
#         print("Datos existentes--> ", resu)
#     else:
#         email = input("Ingrese email : ") #crear función para validar email
#         clave = input("Ingrese clave : ") #crear funci+on para valida clave
#         print(UserDTO().agregarUsuario(username, email,clave))

# def validarLogin():
#     username = input("Ingrese nombre de usuario : ")
#     clave = input("Ingrese contraseña : ")
#     resultado = UserDTO().validarLogin(username, clave)
#     return resultado

#MENÚ PRINCIPAL PRUEBA 
def menuPrincipal():
    print("1 CRUD empleados".center(30,'-'))
    print("2 CRUD cargos".center(30,'-'))
    print("3 CRUD comunas".center(30,'-'))
    print("4 SALIR".center(30),'-')

    opcion =  input("Ingrese una opción : ")
    
    if opcion == 2:
        subMenuDos()


def subMenuDos():
    print("1 Ingresar cargo".center(30,'-'))
    print("2 Modificar cargo".center(30,'-'))
    print("3 Eliminar  cargo".center(30,'-'))
    print("4 Mostrar todos los cargos".center(30,'-'))
    print("5 Volver al menú Principal".center(30,'-'))
def submenuTres():
    print("6 Ingresar comuna".center(30,'-'))
    print("7 Modificar comuna".center(30,'-'))
    print("8 Eliminar comuna".center(30,'-'))
    print("9 Mostrar todas las comunas".center(30,'-'))
    print("10 Volver al menú principal".center(30,'-'))


### para llegar al menu primero hay que loguearse

# def inicial():

#     while True:
#         opc = menu()
#         if opc == 1:
#             listAll()
#         elif opc == 2:
#             validateAddUser()
#         elif opc == 3:
#             #validaDelUser() 
#             pass
#         elif opc == 4:
#             validateUpdateUser()
#         elif opc == 5:
#             validateFindUser()
#         else:
#             break





