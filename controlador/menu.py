from controlador.validations_cargo import *
from controlador.validations_comuna import *
# from controlador.validations_empleado import *



def menuPrincipal():
    while True:
        print('Bienvenido al minimarket fenix \n \n'.center(100,' '))
        print("1 CRUD empleados".center(100,'-'))
        print("2 CRUD cargos".center(100,'-'))
        print("3 CRUD comunas".center(100,'-'))
        print("4 SALIR".center(100),'-')

        opcion =  input("Ingrese una opción : ")
        try:
            opcion = int(opcion)
            if opcion == 1:
                print('no hay nada aquí')
            if opcion == 2:
                subMenuDos()
            if opcion == 3:
                submenuTres()
            if opcion == 4:
                break
            else:
                menuPrincipal()
        except ValueError:
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('INGRESE UNA OPCIÓN VÁLIDA'.center(100,' '))
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            menuPrincipal()
        except KeyboardInterrupt:
            print('ACCIÓN INDEBIDA!!!!'.center(100,'-'))
            menuPrincipal()



def subMenuDos():
    print("1 Ingresar cargo".center(100,'-'))
    print("2 Modificar cargo".center(100,'-'))
    print("3 Eliminar  cargo".center(100,'-'))
    print("4 Mostrar todos los cargos".center(100,'-'))
    print("5 Volver al menú Principal".center(100,'-'))
    
    opcion = input('ingrese una opción'.center(100,'-'))
    try:
        opcion = int(opcion)
        if opcion == 1:
            validarAddCargo()
        if opcion == 2:
            validarUpdateCargo()
        if opcion == 3:
            validarDelCargo()
        if opcion == 4:
            validarMostrarCargos()
        if opcion == 5:
            menuPrincipal()
        else:
            subMenuDos()
    except ValueError:
        print('OPCIÓN INVÁLIDA , INGRESE OTRA POR FAVOR'.center(100,'-'))
        subMenuDos()
    except KeyboardInterrupt:
        print('\n')
        print('\n')
        print('\n')
        print('ACCIÓN INDEBIDA!!!!'.center(100,'-'))
        print('\n')
        print('\n')
        print('\n')
        subMenuDos()






def submenuTres():
    print(" 6 Ingresar comuna".center(100,'-'))
    print(" 7 Modificar comuna".center(100,'-'))
    print(" 8 Eliminar comuna".center(100,'-'))
    print(" 9 Mostrar todas las comunas".center(100,'-'))
    print(" 10 Volver al menú principal".center(100,'-'))

    opcion = input('ingrese una opción'.center(100,'-'))

    try:
        opcion = int(opcion)
        if opcion == 6:
            validateAddComuna()
        if opcion == 7:
            validateUpdateComuna()
        if opcion == 8:
            validateDelComuna()
        if opcion == 9:
            validateListarComunas()
        if opcion == 10:
            menuPrincipal()
    except ValueError:
        
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('OPCIÓN INVÁLIDA , INGRESE OTRA POR FAVOR'.center(100,'-'))
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        subMenuDos()
    except KeyboardInterrupt:
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('ACCIÓN INDEBIDA , INGRESE OTRA POR FAVOR'.center(100,'-'))
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        submenuTres()


#Esta es la función que llama al menú principal
#a través de esta función se validará el usuario y la contraseña
def inicial():
    menuPrincipal()