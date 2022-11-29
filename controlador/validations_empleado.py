from controlador.dto_empleado import EmpleadoDTO


def listAll():
    print("Listado de Empleados")
    resultado = EmpleadoDTO().listarEmpleados()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")

def validateFindEmpleado():
    nombre = input("Ingrese el nombre del empleado a buscar : ")
    if nombre == "":
        print("Nombre de empleado incorrecto")
        return validateFindEmpleado()
    else:
        resu = EmpleadoDTO().buscarEmpleado(nombre)
        if resu is not None:
            print(f"Resultado : {resu}")
        else:
            print("Empleado no encontrado")

def validateUpdateEmpleado():
    run = input("Ingrese el RUN del empleado a modificar: ")
    if len(run) == 0:
        print("Debe ingresar un RUN de empleado")
        return validateUpdateEmpleado()
    resu = EmpleadoDTO().buscarEmpleado(run)
    if resu is not None:
        print("Datos --> ", resu)
        nombre = input("Ingrese nombre: ")
        while (len(nombre) <= 0):
            nombre = input("Ingrese un nombre válido: ")
        apellido = input("Ingrese apellido: ")
        while (len(apellido) <= 0):
            apellido = input("Ingrese un apellido válido: ")
        email = input("Ingrese email: ")
        while (len(email) <= 0):
            email = input("Ingrese un email válido: ")
        clave = input("Ingrese clave: ")
        while (len(clave) <= 0):
            clave = input("Ingrese una clave válida: ")
        direccion = input("Ingrese dirección: ")
        while (len(direccion) <= 0):
            direccion = input("Ingrese una dirección válida: ")
        print(EmpleadoDTO().actualizarEmpleado(nombre, apellido, direccion, clave, email))
    else:
        print("Usuario no encontrado")

def validateAddUser():
    run = input("Ingrese RUN de usuario a incorporar: ")
    if len(run) == 0:
        print("Debe ingresar un nombre de usuario")
        return validateAddUser()
    resu = EmpleadoDTO().buscarEmpleado(run)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:
        nombre = input("Ingrese nombre: ")
        while (len(nombre) <= 0):
            nombre = input("Ingrese un nombre válido: ")
        apellido = input("Ingrese apellido: ")
        while (len(apellido) <= 0):
            apellido = input("Ingrese un apellido válido: ")
        email = input("Ingrese email: ")
        while (len(email) <= 0):
            email = input("Ingrese un email válido: ")
        clave = input("Ingrese clave: ")
        while (len(clave) <= 0):
            clave = input("Ingrese una clave válida: ")
        direccion = input("Ingrese dirección: ")
        while (len(direccion) <= 0):
            direccion = input("Ingrese una dirección válida: ")
        print(UserDTO().agregarUsuario(run, nombre, apellido, cargoN = None, direccion, clave, email, comunaN = None))

def validateDelUser():
    run = input("Ingrese RUN de empleado a eliminar: ")
    if len(run) == 0:
        print("Debe ingresar un RUN de empleado")
        return validateDelUser()
    resu = EmpleadoDTO().buscarEmpleado(run)
    if resu is not None:
        print("Datos existentes--> ", resu)
    else:
        print(UserDTO().eliminarEmpleado(run))

def validarLogin():
    run = input("Ingrese RUN de usuario: ")
    clave = input("Ingrese contraseña: ")
    resultado = UserDTO().validarLogin(run, clave)
    return resultado


def menu():
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Eliminar Usuario")
    print("4. Actualizar Usuario")
    print("5. Buscar Usuario")
    print("6. Salir")
    opc = int( input("Ingrese una opción : "))
    return opc

def inicial():

    while True:
        opc = menu()
        if opc == 1:
            listAll()
        elif opc == 2:
            validateAddEmpleado()
        elif opc == 3:
            validaDelUser()
        elif opc == 4:
            validateUpdateEmpleado()
        elif opc == 5:
            validateFindEmpleado()
        else:
            break

