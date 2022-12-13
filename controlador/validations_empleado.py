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
def validateAddEmpleado():
    try:
        idCargo = input('ingrese el id del cargo')
        idComuna = input('ingrese el ID de la comuna')
        idCargo = int(idCargo)
        idComuna = int(idComuna)
        run = input('ingrese el rut del empleado')
        nombre = input('ingrese tan solo el nombre del empleado')
        apellido = input('ingrese el apellido del empleado')
        direccion= input('ingrese la dirección del empleado')
        clave = input('ingrese  su clave')
        correo = input('ingrese su correo')
        empleado = EmpleadoDTO
        empleado.addEmpleado(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo)
    except:
        print('algo muy malo pasó u.u')

def validateDelEmpleado():
    run = input('ingrese el rut de la persona a eliminar')
    try:
        empleado = EmpleadoDTO
        #por alguna razón al instanciar esta clase con las llaves no funciona :(
        mensaje = empleado.delEmpleado(run)
        print(mensaje)
    except:
        print('el empleado no existe :(')




def validateUpdateEmpleado():
    run = input('ingrese el rut del empleado a modificar')
    nombre = input('ingrese el nombre a modificar')
    apellido = input('ingrese el apellido a modificar')
    direccion = input('ingrese la dirección a modificar')
    idCargo = input('ingrese el id del cargo')
    idComuna = input('ingrese el id de la comuna ')
    
    
    idCargo = int(idCargo)
    idComuna = int(idComuna)
    empleado = EmpleadoDTO
    mensaje = empleado.updateEmpleado(nombre,apellido,direccion,idCargo,idComuna,run)
    print(mensaje)

def validateFindEmpleadoByComuna():
    comuna = input('ingrese el nombre de la comuna')
    try:
        empleado = EmpleadoDTO
        empleado.findEmpleadoByComuna(comuna)
        empleados = empleado.findEmpleadoByComuna(comuna)
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
       


    