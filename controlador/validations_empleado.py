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
        empleado = EmpleadoDTO()
        empleado.addEmpleado(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo)
    except:
        print('algo muy malo pasó u.u')

def validateDelEmpleado():
    run = input('ingrese el rut de la persona a eliminar')
    try:
        empleado = EmpleadoDTO()
        empleado.delEmpleado(run)
    except:
        print('no existe ese empleado al parecer :(')

    