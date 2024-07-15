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

class Carrito:
    def __init__(self):
        self.productos = []
        self.total_precio = 0

    def agregar_producto(self, producto, cantidad):
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
    
    def mostrar_carrito(self):
        print("Carrito:")
        for producto, cantidad in self.productos:
            print(f"    Producto: {producto.nombre}, Cantidad: {cantidad}")
        print(f"    Total Precio: {self.total_precio}")

class Pedido:
    def __init__(self, usuario, productos, estado, fecha, numero_seguimiento):
        if not productos:
            raise CarritoVacio()
        self.usuario = usuario
        self.productos = productos.copy()
        self.estado = estado
        self.fecha = fecha
        self.numero_seguimiento = numero_seguimiento
    
    def mostrar_pedido(self):
        print(f"Pedido-> Usuario: {self.usuario.nombre}, Estado: {self.estado}, Fecha de compra: {self.fecha}, Número de seguimiento: {self.numero_seguimiento}")
        for producto, cantidad in self.productos:
            print(f"    Producto: {producto.nombre}, Cantidad: {cantidad}")

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
        self.carrito = Carrito()

    def __str__(self):
        return f"Cliente-> Nombre: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono}, Ubicación: {self.ubicacion}"

class Pago:
    def __init__(self, usuario, pedido, monto, metodo_pago):
        self.usuario = usuario
        self.pedido = pedido
        self.monto = monto
        self.metodo_pago = metodo_pago

    def __str__(self):
        return f"Pago-> Usuario: {self.usuario.nombre}, Monto: {self.monto}, Método de Pago: {self.metodo_pago}"

def main():
    try:
        #PRODUCTOS
        producto1 = Producto(1, "Joggin", "Perfecto para este verano", 15, 20)
        producto2 = Producto(2, "Buzo", "Perfecto para este invierno", 20, 20)
        producto3 = Producto(3, "Campera", "Campera de invierno", 25, 30)
        producto4 = Producto(4, "Botas", "Perfecto para dias de lluvia", 5, 30)

        #CLIENTE
        cliente1 = Cliente("Homero J. Simpson", "amantedelacomida53@aol.com", "764-84377", "Avenida Siempreviva 742")
        cliente2 = Cliente("Marjorie Jacqueline Simpson", "marge_simpson@nospam.com", "764-84377", "Avenida Siempreviva 742")

        # AGREGAR PRODUCTOS AL CARRITO
        cliente1.carrito.agregar_producto(producto1, 10)
        cliente1.carrito.agregar_producto(producto2, 5)
        cliente2.carrito.agregar_producto(producto3, 5)
        cliente2.carrito.agregar_producto(producto4, 10)
        
        #CREACION DE PEDIDO
        pedido1 = Pedido(cliente1, cliente1.carrito.productos, "Pendiente", "11/07/2024", "AAA1212")
        pedido2 = Pedido(cliente2, cliente2.carrito.productos, "Pagado", "9/05/2024", "BBB2121")

        #PAGO
        pago1 = Pago(cliente1, pedido1, sum(producto.precio * cantidad for producto, cantidad in pedido1.productos), "Tarjeta de Crédito")
        pago2 = Pago(cliente2, pedido2, sum(producto.precio * cantidad for producto, cantidad in pedido2.productos), "Efectivo")

    
        print(cliente1)
        cliente1.carrito.mostrar_carrito()
        pedido1.mostrar_pedido()
        print(pago1)
        print("\n")
        print(cliente2)
        cliente2.carrito.mostrar_carrito()
        pedido2.mostrar_pedido()
        print(pago2)
    except StockInsuficiente as e:
        print(e)
    except ProductoNoEncontrado as e:
        print(e)
    except CarritoVacio as e:
        print(e)

main()
