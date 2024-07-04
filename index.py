#Clase Clientes:
class Cliente:
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
        return f'Cliente: {self.nombre} - Correo: {self.correo_electronico} - Telefono: {self.telefono} - Ubicación: {self.ubicación}.'

#Clase Pago:
class Pago:
    def __init__ (self,id,usuario,pedido,monto,metodo_de_pago):
        self.id = id
        self.usuario = usuario
        self.pedido = pedido
        self.monto = monto
        self.metodo_de_pago = metodo_de_pago

    def __str__(self):
        return f'ID: {self.id} - Usuario: {self.usuario} - Pedido: {self.pedido} - Monto: {self.monto} - Metodo de Pago: {self.metodo_de_pago}.'
    
#Clase Carrito:
class Carrito:
    def __init__(self,id_carrito,productos,total_precios,precio):
        self.id_carrito = Carrito
        self.productos = productos
        self.total_precios = total_precios
        self.precio = precio
    
    def __str__(self):
        return f'IdCarrito: {self.id_carrito} - Productos: {self.productos} - Total_Precios: {self.total_precios} - Precio: {self.precio}.'

#Clase Producto:
class Producto:
    def __init__(self,id_producto,nombre,descripcion,precios):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precios = precios
    
    def __str__(self):
        return f'ID del Producto: {self.id_producto} - Nombre del producto: {self.nombre} - Descripcion: {self-descripcion} - Precios: {self.precios}.'

#Clase Pedido:
class Pedido:
    def __init__(self,id_pedido,usuarios,cant_productos,estado,fecha,nro_seguimiento):
        self.id_pedido = id_pedido
        self.usuarios = usuarios
        self.cant_productos = cant_productos
        self.estado = estado
        self.fecha = fecha
        self.nro_seguimiento = nro_seguimiento

    def __str__(self):
        return f'Id del pedido: {self.id_pedido} - Usuario: {self.usuarios} - Cantidad de Productos: {self.cant_productos} - Estado: {self.estado} - Numero de Seguimiento: {self.nro_seguimiento}.'
