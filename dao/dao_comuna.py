from conex import conn
import traceback


class DaoComuna:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "minimarket_fenix")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def listarComuna(self):

        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("SELECT * FROM COMUNA")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result

    def buscarComuna(self,numero_comuna):
        sql = "SELECT * FROM COMUNA WHERE NUMEROCOMUNA = {0}".format(numero_comuna)
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def modificarComuna(self,nombre_comuna,numero_comuna):
        sql = "UPDATE COMUNA SET NOMBRECOMUNA = '{0}' WHERE NUMEROCOMUNA = {1} ".format(nombre_comuna,numero_comuna)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos modificados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def agregarComuna(self,numeroComuna,nombreComuna):
        sql = "insert into comuna (IDCOMUNA,NUMEROCOMUNA,NOMBRECOMUNA) values (NULL,{0},'{1}')".format(numeroComuna,nombreComuna)
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
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