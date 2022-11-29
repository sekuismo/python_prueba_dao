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
            cursor.execute("select codigoComuna, nombreComuna, descripComuna")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return result

    def buscarComuna(self, comuna):
        sql = "select codigoComuna, nombreComuna, descripComuna from comuna where nombreComuna = %s"
        resultado = None
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (user.username,))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def modificarComuna(self, comuna):
        sql = "update comuna set codigo=%s, password = %s where nombreComuna = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.codigoComuna, comuna.nombreComuna, comuna.descripComuna))
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

    def agregarComuna(self,comuna):
        sql = "insert into comuna (codigoComuna, nombreComuna, descripComuna) values (%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.codigoComuna,comuna.nombreComuna, comuna.descripComuna))
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