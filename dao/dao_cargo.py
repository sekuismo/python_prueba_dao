from conex import conn
import traceback
class DaoCargo:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost","root","", 'minimarket_fenix')
        except Exception as ex:
            print(ex)
        
    def getConex(self):
        return self.conn
    #los métodos toman como parámetro a self, ya que cada vez que se ejecuta se llama 
    # a la conexión a la base de datos

    def findCargo(self,numero_cargo):
        
        
        sentencia_sql = "SELECT * FROM CARGO WHERE NUMEROCARGO = {0}".format(numero_cargo)
        resultado = None
        conexion = self.getConex()

        try:
            cursor = conexion.getConex().cursor()
            cursor.execute(sentencia_sql)
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if conexion.getConex().is_connected():
                conexion.closeConex()
        return resultado



    def addCargo(self,num_cargo,nombre_cargo):

        sentencia_sql = "INSERT INTO CARGO VALUES(NULL,{0},'{1}');".format(num_cargo,nombre_cargo)
        conexion = self.getConex()
        try:
            cursor = conexion.getConex().cursor()
            cursor.execute(sentencia_sql)
            conexion.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intent arlo"
            print('algo no funciona wm')
        finally:
            if conexion.getConex().is_connected():
                conexion.closeConex()
        return mensaje
    # else:
    #     print('el cargo ya existe, inténtelo de nuevo')
    #     self.addCargo

    def updateCargo(self,num_cargo,nombre_cargo):
        #este método solo permite modificar el nombre del cargo, al cual se accede a través de ingresar 
        #el número de cargo a modificar

        sentencia_sql = "UPDATE CARGO SET  NOMBRECARGO ='{0}'  WHERE NUMEROCARGO ={1};".format(nombre_cargo,num_cargo)
        conexion = self.getConex()
        try:
            cursor = conexion.getConex().cursor()
            cursor.execute(sentencia_sql)
            conexion.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Actualizado correctamente!"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos...  vuelva a intentarlo"
        finally:
            if conexion.getConex().is_connected():
                conexion.closeConex()
        return mensaje

    def delCargo(self,num_cargo):
        
        sentencia_sql = "DELETE  FROM CARGO WHERE NUMEROCARGO ={0}".format(num_cargo)
        conexion = self.getConex()

        try:
            cursor = conexion.getConex().cursor()
            cursor.execute(sentencia_sql)
            conexion.getConex().commit()
            mensaje = "eliminado correctamente"
        except:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intent arlo"
        finally:
            if conexion.getConex().is_connected():
                conexion.closeConex()
        return mensaje

    # def listarUsuarios(self):

    #     c = self.getConex()
    #     result = None
    #     try:
    #         cursor = c.getConex().cursor()
    #         cursor.execute("select username, email, password, create_time from users")
    #         result = cursor.fetchall()
    #     except Exception as ex:
    #         print(ex)
    #     finally:
    #         if c.getConex().is_connected():
    #             c.closeConex()

    #     return result

    def findAllCargos(self):
        sentencia_sql = "SELECT NUMEROCARGO, NOMBRECARGO FROM CARGO"
        conexion = self.getConex()
        try:
            cursor = conexion.getConex().cursor(buffered=True)
            cursor.execute(sentencia_sql)
            conexion.getConex().commit()
            resultado = cursor.fetchall()
        except:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if conexion.getConex().is_connected():
                conexion.closeConex()
             
        return resultado









#importante considerar que cada método recibe parámetros , los cuales son definidos
# por el diagrama de clases , estos parámetros se obtienen a través de "inputs"
# y se escriben en el módulo validaciones 
# para que al ser validados sean llamados por el DTO de cada clase
#el mismo DTO es quien imprime la clase a través de cargar los datos 



