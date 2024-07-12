class StockInsuficiente(Exception):
    def __init__(self, producto, cantidad_disponible):
        super().__init__(f"No hay suficiente stock para el producto '{producto.nombre}'. Stock disponible: {cantidad_disponible}")

class ProductoNoEncontrado(Exception):
    def __init__(self, producto):
        super().__init__(f"El producto '{producto.nombre}' no se encuentra en el carrito.")

class CarritoVacio(Exception):
    def __init__(self):
        super().__init__("El carrito está vacío. No se puede crear un pedido sin productos.")

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto(ID: {self.id_producto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock})"

class Carrito:
    def __init__(self, id_carrito):
        self.id_carrito = id_carrito
        self.productos = []
        self.total_precio = 0

    def agregar_producto(self, producto, cantidad=1):
        if cantidad <= producto.stock:
            self.productos.append((producto, cantidad))
            self.total_precio = self.total_precio + producto.precio * cantidad
            producto.stock = producto.stock - cantidad
        else:
            raise StockInsuficiente(producto, producto.stock)

    def quitar_producto(self, producto):
        for prod, cantidad in self.productos:
            if prod == producto:
                self.productos.remove((prod, cantidad))
                self.total_precio = self.total_precio - prod.precio * cantidad
                producto.stock = producto.stock + cantidad
                return
        raise ProductoNoEncontrado(producto)

    def __str__(self):
        productos_str = "\n".join(f"{producto.nombre} (Cantidad: {cantidad})" for producto, cantidad in self.productos)
        return f"Carrito(ID: {self.id_carrito}, Productos: [{productos_str}], Total Precio: {self.total_precio})"

class Pedido:
    def __init__(self, id_pedido, usuario, productos, estado, fecha, numero_seguimiento):
        if not productos:
            raise CarritoVacio()
        self.id_pedido = id_pedido
        self.usuario = usuario
        self.productos = productos
        self.estado = estado
        self.fecha = fecha
        self.numero_seguimiento = numero_seguimiento

    def __str__(self):
        productos_str = ", ".join(f"{producto.nombre} (Cantidad: {cantidad})" for producto, cantidad in self.productos)
        return (f"Pedido(ID: {self.id_pedido}, Usuario: {self.usuario.nombre}, Productos: [{productos_str}], "
                f"Estado: {self.estado}, Fecha: {self.fecha}, Número de Seguimiento: {self.numero_seguimiento})")

class Usuario:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"Usuario(Nombre: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono})"

class Cliente(Usuario):
    def __init__(self, nombre, correo, telefono, ubicacion):
        super().__init__(nombre, correo, telefono)
        self.ubicacion = ubicacion
        self.carrito = Carrito(id_carrito=1)

    def __str__(self):
        return f"Cliente(Nombre: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono}, Ubicación: {self.ubicacion}, Carrito: {self.carrito})"

class Pago:
    def __init__(self, id_pago, usuario, pedido, monto, metodo_pago):
        self.id_pago = id_pago
        self.usuario = usuario
        self.pedido = pedido
        self.monto = monto
        self.metodo_pago = metodo_pago

    def __str__(self):
        return (f"Pago(ID: {self.id_pago}, Usuario: {self.usuario.nombre}, Pedido ID: {self.pedido.id_pedido}, "
                f"Monto: {self.monto}, Método de Pago: {self.metodo_pago})")

try:
    # Crear algunos productos
    producto1 = Producto(1, "Joggin", "Perfecto para este verano", 30, 10)
    producto2 = Producto(2, "Buzo", "Perfecto para temporada de invierno", 25, 5)
    #producto3 = Producto(3, "Campera", "Perfecto para salir a caminar", 25, 10)

    # Crear un cliente (usuario registrado)
    cliente = Cliente("Juan Perez", "juan@example.com", "123456789", "Calle Falsa 123")

    # Cliente intenta agregar productos al carrito
    cliente.carrito.agregar_producto(producto1, 2)
    cliente.carrito.agregar_producto(producto2, 2)  # Esto debería lanzar una excepción

    # Cliente intenta quitar un producto del carrito
    cliente.carrito.quitar_producto(producto1)
    #cliente.carrito.quitar_producto(producto2)  # Esto debería lanzar una excepción

    # Crear un pedido
    pedido = Pedido(1, cliente, cliente.carrito.productos, "Pendiente", "2024-07-11", "123ABC")

    # Crear un pago
    pago = Pago(1, cliente, pedido, cliente.carrito.total_precio, "Tarjeta de Crédito")

    # Imprimir detalles pertinentes
    print(cliente)
    print(cliente.carrito)
    print(pedido)
    print(pago)
except StockInsuficiente as e:
    print(e)
except ProductoNoEncontrado as e:
    print(e)
except CarritoVacio as e:
    print(e)
