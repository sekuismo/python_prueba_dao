from conex import conn
import traceback

class daoEmpleado:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "mydb")
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

    def actualizarEmpleado(self, empleado): #  no se si modificar los IDs
        sql = "UPDATE EMPLEADO SET NOMBRE = %s APELLIDO = %s DIRECCION = %s CLAVE = %s CORREO = %s WHERE RUN = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado(), empleado.getRunEmpleado()))
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

    def agregarEmpleado(self, empleado):
        sql = "INSERT INTO EMPLEADO (IDCARGO, IDCOMUNA, RUN, NOMBRE, APELLIDO, DIRECCION, CLAVE, CORREO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor() # Falta la clase cargo pal método get codigo:
            cursor.execute(sql, (empleado.getCargo().getCodigoCargo(), empleado.getComuna().getCodigoComuna(), empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado()))
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

    def eliminarEmpleado(self, empleado):
        sql = "DELETE FROM EMPLEADO WHERE RUN=%s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getRunEmpleado(),))
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

