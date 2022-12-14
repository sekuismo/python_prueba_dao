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


    def findEmpleadoByCargo(self,nombre_cargo):
        resultado = None
        try:
            sql ="SELECT e.RUN, e.NOMBRE, e.APELLIDO, c.NOMBRECARGO, e.DIRECCION, e.CORREO, co.NOMBRECOMUNA FROM EMPLEADO e INNER JOIN CARGO c ON e.IDCARGO = c.IDCARGO INNER JOIN COMUNA co ON e.IDCOMUNA = co.IDCOMUNA WHERE c.NOMBRECARGO ='{0}' ".format(nombre_cargo)
            
            c = self.getConex()
            cursor = c.getConex().cursor() 
            cursor.execute(sql)
            resultado = cursor.fetchall()
            c.getConex().commit()

        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
            return resultado



