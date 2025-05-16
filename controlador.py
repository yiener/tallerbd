from modelo import Modelo
from vista import VistaPrincipal

class Controlador:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo()
        self.vista = VistaPrincipal(root, self)

    def obtener_productos(self):
        return self.modelo.obtener_productos()

    def obtener_producto(self, id_producto):
        productos = self.modelo.obtener_productos()
        for p in productos:
            if p[0] == id_producto:
                return p
        return None

    def crear_producto(self, nombre, precio, stock, categoria):
        if self.modelo.crear_producto(nombre, precio, stock, categoria):
            self.vista.actualizar_lista_productos()
            return True
        return False

    def actualizar_producto(self, id_producto, nombre, precio, stock, categoria):
        if self.modelo.actualizar_producto(id_producto, nombre, precio, stock, categoria):
            self.vista.actualizar_lista_productos()
            return True
        return False

    def eliminar_producto(self, id_producto):
        if self.modelo.eliminar_producto(id_producto):
            self.vista.actualizar_lista_productos()
            return True
        return False

    def obtener_clientes(self):
        return self.modelo.obtener_clientes()

    def obtener_cliente(self, id_cliente):
        clientes = self.modelo.obtener_clientes()
        for c in clientes:
            if c[0] == id_cliente:
                return c
        return None

    def crear_cliente(self, nombre, apellidos, email):
        if self.modelo.crear_cliente(nombre, apellidos, email):
            self.vista.actualizar_lista_clientes()
            return True
        return False

    def actualizar_cliente(self, id_cliente, nombre, apellidos, email):
        if self.modelo.actualizar_cliente(id_cliente, nombre, apellidos, email):
            self.vista.actualizar_lista_clientes()
            return True
        return False

    def eliminar_cliente(self, id_cliente):
        if self.modelo.eliminar_cliente(id_cliente):
            self.vista.actualizar_lista_clientes()
            return True
        return False

    def obtener_informe_inventario(self):
        return self.modelo.obtener_informe_inventario()

    def obtener_informe_por_categoria(self):
        return self.modelo.obtener_informe_por_categoria()

    def obtener_productos_stock_bajo(self, limite=10):
        return self.modelo.obtener_productos_stock_bajo(limite)

    def obtener_total_compras_cliente(self, id_cliente):
        return self.modelo.obtener_total_compras_cliente(id_cliente)

    def obtener_total_compras(self):
        return self.modelo.obtener_total_compras()