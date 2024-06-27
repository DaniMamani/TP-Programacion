class Clientes:
    def __init__ (self, nombre, correo_electronico, telefono, ubicación):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.ubicación
        self.registrado = False
        self.sesion_iniciada = False
    
    def registrarse(self):
        if not self.registrado:
            self.registrado = True
            return f"{self.nombre} se ha registrado con exito."
        else:
            return f"{self.nombre} ya esta registrado."
    
    def iniciarSesion(self, correo, telefono):
        if self.registrado:
            if self.correo_electronico == correo and self.telefono == telefono:
                self.sesion_iniciada = True
                return f"{self.nombre} ha iniciado sesion con exito."
            else:
                return "Correo eletronico o telefono incorrecto."
        else:
            return "El cliente ya esta registrado."
    
    def comprar(self):
        if self.sesion_iniciada:
            return f"{self.nombre} ha realizado una compra."
        else: 
            return "Por favor, inicie sesion para realizar una compra."
    
    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo_electronico}, Telefono: {self.telefono}, Ubicación: {self.ubicación}"