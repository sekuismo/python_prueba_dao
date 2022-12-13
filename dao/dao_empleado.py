from conex import conn
import traceback

class daoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "minimarket_fenix")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def listarEmpleados(self): # No se si mostrar los IDs
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor() # Tuve que mostrar la clave para usarla en el DTO
            cursor.execute("SELECT RUN, NOMBRE, APELLIDO, DIRECCION, CLAVE, CORREO FROM EMPLEADO")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result

    def buscarEmpleado(self, empleado): # No se si mostrar los IDs, tuve que mostrar clave para DTO
        sql = "SELECT RUN, NOMBRE, APELLIDO, DIRECCION, CLAVE, CORREO FROM EMPLEADO WHERE RUN = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getRunEmpleado(),))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def validarLogin(self, empleado):
        sql = "SELECT RUN FROM EMPLEADO WHERE RUN = %s AND CLAVE = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getRunEmpleado(), empleado.getClaveEmpleado()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado






    def updateEmpleado(self,nombre,apellido,direccion,idCargo,idComuna,run): 
        sql = "UPDATE EMPLEADO SET NOMBRE ='{0}' ,APELLIDO ='{1}' ,DIRECCION ='{2}' ,IDCARGO ={3} ,IDCOMUNA = {4}  WHERE RUN ='{5}'".format(nombre,apellido,direccion,idCargo,idComuna,run)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Datos modificados satisfactoriamente"
            else:
                mensaje= "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje


    # importante considerar select idcargo from cargo where nombre 
    # así se puede ingresear el nombre del cargo y después hacer que retorne el id del cargo
    #y ese id almacenarlo en la tabla empleado 
    
    def addEmpleado(self,idCargo,idComuna,run,nombre,apellido,direccion,clave,correo):
        sql = "INSERT INTO EMPLEADO (IDCARGO, IDCOMUNA, RUN, NOMBRE, APELLIDO, DIRECCION, CLAVE, CORREO) VALUES ({0},{1},'{2}','{3}','{4}','{5}','{6}','{7}')".format(idCargo,idComuna,run,nombre,apellido,direccion,clave,correo)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor() # Falta la clase cargo pal método get codigo:
            cursor.execute(sql)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios" 
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def delEmpleado(self,run):
        sql = "DELETE FROM EMPLEADO WHERE RUN ='{0}' ".format(run)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Eliminado satisfactoriamente"
            else:
                mensaje="No se realizaron cambios" 
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
        



    def findEmpleadoByComuna(self,nombre_comuna):
        sql = "SELECT e.RUN, e.NOMBRE, e.APELLIDO, c.NOMBRECARGO, e.DIRECCION, e.CORREO, co.NOMBRECOMUNA FROM EMPLEADO e JOIN CARGO c ON e.IDCARGO = c.IDCARGO JOIN COMUNA co ON e.IDCOMUNA = co.IDCOMUNA WHERE co.NOMBRECOMUNA ='{0}'".format(nombre_comuna)
        c = self.getConex()
        try:
            cursor = c.getConex().cursor() # Falta la clase cargo pal método get codigo:
            cursor.execute(sql)
            resultado = cursor.fetchall()
            c.getConex().commit()



        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado



# El error que se muestra en tu código indica que se ha producido un fallo al agregar o actualizar un registro en una tabla de la 
# base de datos debido a una violación de la restricción de clave externa.

# La restricción de clave externa es una característica de las bases de datos
#  relacionales que se utiliza para asegurar la integridad de los datos.
#   Esta restricción impide que se agreguen o actualicen registros en una
#    tabla si los datos que se intentan agregar o actualizar violan la relación entre las tablas.

# En este caso, el error se refiere a una restricción de clave externa en
#  la tabla empleado, que tiene una columna llamada IDCARGO que se relaciona
#   con la tabla cargo. La restricción de clave externa especifica que la 
#   columna IDCARGO en la tabla empleado debe contener valores que existan
#    en la columna IDCARGO en la tabla cargo. Esto significa que,
#     si intentamos agregar o actualizar un registro en la tabla 
#     empleado con un valor en la columna IDCARGO que no existe
#      en la tabla cargo, se producirá un error.

# Para solucionar este error, debes asegurarte de que el valor 
# que estás intentando agregar o actualizar en la columna IDCARGO 
# de la tabla empleado exista en la tabla cargo. Por ejemplo,
#  si intentas agregar un nuevo empleado con un cargo que no
#   existe en la tabla cargo, debes primero agregar el cargo 
#   a la tabla cargo antes de agregar el empleado a la tabla empleado.
#    Si necesitas más ayuda para solucionar este error, no dudes en preguntar.