import sqlite3

class Modelo:
    def __init__(self):
        self.conn = sqlite3.connect('tienda.db')
        self.crear_tablas()
    
    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            historial_compras REAL DEFAULT 0
        )''')
        self.conn.commit()

    def crear_producto(self, nombre, precio, stock, categoria):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO productos VALUES (NULL,?,?,?,?)', 
                          (nombre, precio, stock, categoria))
            self.conn.commit()
            return True
        except:
            return False

    def obtener_productos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall()

    def actualizar_producto(self, id_producto, nombre, precio, stock, categoria):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            UPDATE productos 
            SET nombre=?, precio=?, stock=?, categoria=?
            WHERE id=?
            ''', (nombre, precio, stock, categoria, id_producto))
            self.conn.commit()
            return cursor.rowcount > 0
        except:
            return False

    def eliminar_producto(self, id_producto):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM productos WHERE id=?', (id_producto,))
            self.conn.commit()
            return cursor.rowcount > 0
        except:
            return False

    def crear_cliente(self, nombre, apellidos, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO clientes VALUES (NULL,?,?,?,0)', 
                          (nombre, apellidos, email))
            self.conn.commit()
            return True
        except:
            return False

    def obtener_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()

    def actualizar_cliente(self, id_cliente, nombre, apellidos, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            UPDATE clientes 
            SET nombre=?, apellidos=?, email=?
            WHERE id=?
            ''', (nombre, apellidos, email, id_cliente))
            self.conn.commit()
            return cursor.rowcount > 0
        except:
            return False

    def eliminar_cliente(self, id_cliente):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM clientes WHERE id=?', (id_cliente,))
            self.conn.commit()
            return cursor.rowcount > 0
        except:
            return False

    def obtener_informe_inventario(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(precio * stock) FROM productos')
        return cursor.fetchone()[0] or 0

    def obtener_informe_por_categoria(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT categoria, SUM(precio * stock) 
        FROM productos 
        GROUP BY categoria
        ''')
        return cursor.fetchall()

    def obtener_productos_stock_bajo(self, limite=10):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE stock < ?', (limite,))
        return cursor.fetchall()

    def obtener_total_compras_cliente(self, id_cliente):
        cursor = self.conn.cursor()
        cursor.execute('SELECT historial_compras FROM clientes WHERE id=?', (id_cliente,))
        return cursor.fetchone()[0] or 0

    def obtener_total_compras(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(historial_compras) FROM clientes')
        return cursor.fetchone()[0] or 0