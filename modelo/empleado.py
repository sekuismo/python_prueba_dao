# from cargo import Cargo
# from comuna import Comuna

class Empleado:
    # Constructor:
    def __init__(self, runEmpleado = "", nombreEmpleado = "", apellidoEmpleado = "", cargo = None, direccionEmpleado = "", claveEmpleado = "", correoEmpleado = "", comuna = None):
        self.runEmpleado = runEmpleado
        self.nombreEmpleado = nombreEmpleado
        self.apellidoEmpleado = apellidoEmpleado
        self.cargo = cargo
        self.direccionEmpleado = direccionEmpleado
        self.claveEmpleado = claveEmpleado
        self.correoEmpleado = correoEmpleado
        self.comuna = comuna

    # Getters y setters:
    def getRunEmpleado(self):
        return self.runEmpleado

    def getNombreEmpleado(self):
        return self.nombreEmpleado
        
    def getApellidoEmpleado(self):
        return self.apellidoEmpleado
    
    def getCargo(self):
        return self.cargo
    
    def getDireccionEmpleado(self):
        return self.direccionEmpleado

    def getClaveEmpleado(self):
        return self.claveEmpleado

    def getCorreoEmpleado(self):
        return self.correoEmpleado

    def getComuna(self):
        return self.comuna
    
    def setRunEmpleado(self, run):
        self.runEmpleado = run

    def setNombreEmpleado(self, nombre):
        self.nombreEmpleado = nombre
        
    def setApellidoEmpleado(self, apellido):
        self.apellidoEmpleado = apellido
    
    def setCargo(self, cargo):
        self.cargo = cargo
    
    def setDireccionEmpleado(self, direccion):
        self.direccionEmpleado = direccion

    def setClaveEmpleado(self, clave):
        self.claveEmpleado = clave

    def setCorreoEmpleado(self, correo):
        self.correoEmpleado = correo

    def setComuna(self, comuna):
        self.comuna = comuna

    # Validar login:
    def validarLogin(correo, clave):
        if (correo == self.correoEmpleado and clave == self.claveEmpleado):
            return self
        else:
            return None
    
     # Método str:
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.runEmpleado, self.nombreEmpleado, self.apellidoEmpleado, self.cargo, self.direccionEmpleado, self.claveEmpleado, self.correoEmpleado, self.comuna)