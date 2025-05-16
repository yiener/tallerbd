import tkinter as tk
from tkinter import ttk, messagebox

class VistaPrincipal:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Sistema de Gestión de Tienda")
        self.configurar_interfaz()

    def configurar_interfaz(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.frame_productos = ttk.Frame(self.notebook)
        self.frame_clientes = ttk.Frame(self.notebook)
        self.frame_informes = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_productos, text="Productos")
        self.notebook.add(self.frame_clientes, text="Clientes")
        self.notebook.add(self.frame_informes, text="Informes")

        self.configurar_productos()
        self.configurar_clientes()
        self.configurar_informes()

    def configurar_productos(self):
        frame = ttk.Frame(self.frame_productos)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_productos = ttk.Treeview(frame, columns=('id', 'nombre', 'precio', 'stock', 'categoria'))
        self.tree_productos.heading('#0', text='ID')
        self.tree_productos.column('#0', width=50)
        self.tree_productos.heading('#1', text='Nombre')
        self.tree_productos.heading('#2', text='Precio')
        self.tree_productos.heading('#3', text='Stock')
        self.tree_productos.heading('#4', text='Categoría')
        self.tree_productos.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=5)

        ttk.Button(button_frame, text="Nuevo", command=self.mostrar_formulario_producto).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Editar", command=self.editar_producto).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Eliminar", command=self.eliminar_producto).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_lista_productos).pack(side=tk.LEFT, padx=2)

    def configurar_clientes(self):
        frame = ttk.Frame(self.frame_clientes)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_clientes = ttk.Treeview(frame, columns=('id', 'nombre', 'apellidos', 'email', 'historial'))
        self.tree_clientes.heading('#0', text='ID')
        self.tree_clientes.column('#0', width=50)
        self.tree_clientes.heading('#1', text='Nombre')
        self.tree_clientes.heading('#2', text='Apellidos')
        self.tree_clientes.heading('#3', text='Email')
        self.tree_clientes.heading('#4', text='Historial')
        self.tree_clientes.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=5)

        ttk.Button(button_frame, text="Nuevo", command=self.mostrar_formulario_cliente).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Editar", command=self.editar_cliente).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Eliminar", command=self.eliminar_cliente).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_lista_clientes).pack(side=tk.LEFT, padx=2)

    def configurar_informes(self):
        frame = ttk.Frame(self.frame_informes)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Button(frame, text="Valor Total Inventario", command=self.mostrar_informe_inventario).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="Valor por Categoría", command=self.mostrar_informe_categorias).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="Productos con Stock Bajo", command=self.mostrar_stock_bajo).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="Total Compras por Cliente", command=self.mostrar_compras_cliente).pack(fill=tk.X, pady=5)
        ttk.Button(frame, text="Valor Total de Compras", command=self.mostrar_total_compras).pack(fill=tk.X, pady=5)

    def actualizar_lista_productos(self, productos=None):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        productos = productos or self.controlador.obtener_productos()
        for prod in productos:
            self.tree_productos.insert('', 'end', iid=prod[0], text=prod[0],
                                      values=(prod[1], prod[2], prod[3], prod[4]))

    def actualizar_lista_clientes(self, clientes=None):
        for item in self.tree_clientes.get_children():
            self.tree_clientes.delete(item)
        clientes = clientes or self.controlador.obtener_clientes()
        for cli in clientes:
            self.tree_clientes.insert('', 'end', iid=cli[0], text=cli[0],
                                    values=(cli[1], cli[2], cli[3], cli[4]))

    def mostrar_formulario_producto(self, producto=None):
        top = tk.Toplevel(self.root)
        top.title("Nuevo Producto" if not producto else "Editar Producto")

        frame = ttk.Frame(top, padding=10)
        frame.pack()

        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        nombre = tk.Entry(frame)
        nombre.grid(row=0, column=1)
        
        tk.Label(frame, text="Precio:").grid(row=1, column=0, sticky="e")
        precio = tk.Entry(frame)
        precio.grid(row=1, column=1)
        
        tk.Label(frame, text="Stock:").grid(row=2, column=0, sticky="e")
        stock = tk.Entry(frame)
        stock.grid(row=2, column=1)
        
        tk.Label(frame, text="Categoría:").grid(row=3, column=0, sticky="e")
        categoria = tk.Entry(frame)
        categoria.grid(row=3, column=1)

        if producto:
            nombre.insert(0, producto[1])
            precio.insert(0, producto[2])
            stock.insert(0, producto[3])
            categoria.insert(0, producto[4])

        def guardar():
            if producto:
                self.controlador.actualizar_producto(
                    producto[0],
                    nombre.get(),
                    float(precio.get()),
                    int(stock.get()),
                    categoria.get()
                )
            else:
                self.controlador.crear_producto(
                    nombre.get(),
                    float(precio.get()),
                    int(stock.get()),
                    categoria.get()
                )
            top.destroy()
            self.actualizar_lista_productos()

        ttk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)

    def mostrar_formulario_cliente(self, cliente=None):
        top = tk.Toplevel(self.root)
        top.title("Nuevo Cliente" if not cliente else "Editar Cliente")

        frame = ttk.Frame(top, padding=10)
        frame.pack()

        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        nombre = tk.Entry(frame)
        nombre.grid(row=0, column=1)
        
        tk.Label(frame, text="Apellidos:").grid(row=1, column=0, sticky="e")
        apellidos = tk.Entry(frame)
        apellidos.grid(row=1, column=1)
        
        tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
        email = tk.Entry(frame)
        email.grid(row=2, column=1)

        if cliente:
            nombre.insert(0, cliente[1])
            apellidos.insert(0, cliente[2])
            email.insert(0, cliente[3])

        def guardar():
            if cliente:
                self.controlador.actualizar_cliente(
                    cliente[0],
                    nombre.get(),
                    apellidos.get(),
                    email.get()
                )
            else:
                self.controlador.crear_cliente(
                    nombre.get(),
                    apellidos.get(),
                    email.get()
                )
            top.destroy()
            self.actualizar_lista_clientes()

        ttk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=10)

    def editar_producto(self):
        seleccionado = self.tree_productos.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return
        producto = self.controlador.obtener_producto(seleccionado[0])
        if producto:
            self.mostrar_formulario_producto(producto)

    def eliminar_producto(self):
        seleccionado = self.tree_productos.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este producto?"):
            if self.controlador.eliminar_producto(seleccionado[0]):
                self.actualizar_lista_productos()

    def editar_cliente(self):
        seleccionado = self.tree_clientes.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        cliente = self.controlador.obtener_cliente(seleccionado[0])
        if cliente:
            self.mostrar_formulario_cliente(cliente)

    def eliminar_cliente(self):
        seleccionado = self.tree_clientes.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este cliente?"):
            if self.controlador.eliminar_cliente(seleccionado[0]):
                self.actualizar_lista_clientes()

    def mostrar_informe_inventario(self):
        total = self.controlador.obtener_informe_inventario()
        messagebox.showinfo("Valor Total Inventario", f"Valor total: ${total:,.2f}")

    def mostrar_informe_categorias(self):
        categorias = self.controlador.obtener_informe_por_categoria()
        mensaje = "\n".join([f"{cat[0]}: ${cat[1]:,.2f}" for cat in categorias])
        messagebox.showinfo("Valor por Categoría", mensaje)

    def mostrar_stock_bajo(self):
        productos = self.controlador.obtener_productos_stock_bajo()
        if productos:
            mensaje = "Productos con stock bajo:\n\n"
            mensaje += "\n".join([f"{p[1]} (Stock: {p[3]})" for p in productos])
        else:
            mensaje = "No hay productos con stock bajo"
        messagebox.showinfo("Productos con Stock Bajo", mensaje)

    def mostrar_compras_cliente(self):
        seleccionado = self.tree_clientes.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        total = self.controlador.obtener_total_compras_cliente(seleccionado[0])
        messagebox.showinfo("Total Compras Cliente", f"Total compras: ${total:,.2f}")

    def mostrar_total_compras(self):
        total = self.controlador.obtener_total_compras()
        messagebox.showinfo("Valor Total de Compras", f"Total compras: ${total:,.2f}")