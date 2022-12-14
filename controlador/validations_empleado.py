from controlador.dto_empleado import EmpleadoDTO

#módulo de validación de empleados

def listAll():
    print("Listado de Empleados")
    resultado = EmpleadoDTO().listarEmpleados()
    if len(resultado) > 0:
        for u in resultado:
            print(u)
    else:
        print("no hay resultados")
#si es que no existe el idcargo ni el idcomuna habrá conflicto con llaves
#Está validado que ningún campo esté vacío
def validateAddEmpleado():
    print("ES OBLIGATORIO QUE AL INGRESAR AL EMPLEADO EL ID DEL CARGO Y EL ID DE LA COMUNA EXISTAN".center(50,'-'))
    try:
        idCargo = input('ingrese el id del cargo')
        if idCargo == "":
            print('EL CARGO NO PUEDE ESTAR VACÍO')
            validateAddEmpleado()
        else:
            idComuna = input('ingrese el ID de la comuna')
            if idComuna == "":
                print('EL ID DE LA COMUNA NO PUEDE ESTAR VACÍO')
                validateAddEmpleado()
            else:
                idCargo = int(idCargo)
                idComuna = int(idComuna)
                run = input('ingrese el rut del empleado')
                if run == "":
                    print('EL RUT NO PUEDE ESTAR VACÍO')
                    validateAddEmpleado()
                else:
                    nombre = input('ingrese tan solo el nombre del empleado')
                    if nombre == "":
                        print('EL NOMBRE NO PUEDE ESTAR VACÍO')
                        validateAddEmpleado()
                    else:
                        apellido = input('ingrese el apellido del empleado')
                        if apellido == "":
                            print('EL APELLIDO NO PUEDE ESTAR VACÍO')
                        else:
                            direccion= input('ingrese la dirección del empleado')
                            if direccion == "":
                                print('LA DIRECCIÓN NO PUEDE ESTAR VACÍA')
                                validateAddEmpleado()
                            else:
                                clave = input('ingrese  su clave')
                                if clave =="":
                                    print('LA CLAVE NO PUEDE ESTAR VACÍA')
                                    validateAddEmpleado()
                                else:
                                    correo = input('ingrese su correo')
                                    if correo =="":
                                        print('EL CORREO NO PUEDE SER ESTAR VACÍO')
                                        validateAddEmpleado()
                                    else:
                                        empleado = EmpleadoDTO
                                        resultado = empleado.addEmpleado(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo)
                                        print(resultado)
    except:                             
        print('algo muy malo pasó u.u')

#validación realizada
def validateDelEmpleado():
    run = input('ingrese el rut de la persona a eliminar')
    if run =="":
        print('NO PUEDE ESTAR VACÍO EL RUT')
        validateDelEmpleado()
    else:
        try:
            empleado = EmpleadoDTO
            #por alguna razón al instanciar esta clase con las llaves no funciona :(
            mensaje = empleado.delEmpleado(run)
            print(mensaje)
        except:
            print('el empleado no existe ')



#validación realizada
def validateUpdateEmpleado():
    run = input('ingrese el rut del empleado a modificar')
    if run =="":
        print('NO PUEDE ESTAR VACÍO EL RUT')
        validateUpdateEmpleado()
    else:
        nombre = input('ingrese el nombre a modificar')
        if nombre =="":
            print('NO PUEDE ESTAR VACÍO EL NOMBRE')
            validateUpdateEmpleado()
        else:
            apellido = input('ingrese el apellido a modificar')
            if apellido =="":
                print('NO PUEDE ESTAR VACÍO EL APELLIDO')
                validateUpdateEmpleado()
            else:
                direccion = input('ingrese la dirección a modificar')
                if direccion =="":
                    print('NO PUEDE SER UNA DIRECCIÓN VACÍA')
                    validateUpdateEmpleado()
                else:
                    idCargo = input('ingrese el id del cargo')
                    if idCargo =="":
                        print('EL ID DEL CARGO NO PUEDE SER VACÍO')
                        validateUpdateEmpleado()
                    else:
                        idComuna = input('ingrese el id de la comuna ')
                        if idComuna =="":
                            print('EL ID DE LA COMUNA NO PUEDE ESTAR VACÍO')
                            validateUpdateEmpleado()
                        else:
                            idCargo = int(idCargo)
                            idComuna = int(idComuna)
                            empleado = EmpleadoDTO
                            mensaje = empleado.updateEmpleado(nombre,apellido,direccion,idCargo,idComuna,run)
                            print(mensaje)

def validateFindEmpleadoByComuna():
    comuna = input('ingrese el nombre de la comuna:   ')
    try:
        empleado = EmpleadoDTO
        empleado.findEmpleadoByComuna(comuna)
        empleados = empleado.findEmpleadoByComuna(comuna)
        #si es que es una lista vacía significa que la BD no devolvió nada 
        if empleados == []:
            print('No existen empleados en esa comuna')
        else:
            for datos in empleados:
                run = datos[0]
                nombre = datos[1]
                apellido = datos[2]
                cargo = datos[3]
                direccion = datos[4]
                correo = datos[5]
                comuna = datos[6]
                print("Run: {} \nNombre: {} \nApellido: {} \nCargo: {} \nDireccion: {} \nCorreo: {} \nComuna: {}".format(run, nombre, apellido, cargo, direccion, correo, comuna))
                print('\n \n')
    except:
        print("no funka")

def validateFindEmpleadoByCargo():
    cargo = input('ingrese el nombre del cargo a buscar:   ')

    empleado = EmpleadoDTO
    empleados = empleado.findEmpleadoByCargo(cargo)
    #si es que es una lista vacía significa que la BD no devolvió nada 
    if empleados ==[]:
        print('no existen empleados para ese cargo o no existe el cargo')
    else:
        try:
            for datos in empleados:
                run = datos[0]
                nombre = datos[1]
                apellido = datos[2]
                cargo = datos[3]
                direccion = datos[4]
                correo = datos[5]
                comuna = datos[6]
                print("Run: {} \nNombre: {} \nApellido: {} \nCargo: {} \nDireccion: {} \nCorreo: {} \nComuna: {}".format(run, nombre, apellido, cargo, direccion, correo, comuna))
                print('\n \n')
        except:
            pass

       


    