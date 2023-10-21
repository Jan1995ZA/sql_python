import tkinter as tk
from Conectar import conectar_listar

def mostrar_productos():
    # Crear la ventana principal
    app = tk.Tk()
    app.title("Listado de Productos")

    

    # Crear una función para cargar y mostrar los productos en una ventana
    def mostrar_producto():
        productos = conectar_listar()

        if productos:
            # Crear una nueva ventana para mostrar los productos
            lista_productos_window = tk.Tk()
            lista_productos_window.title("Listado de Productos")

            # Crear un marco para organizar los elementos
            frame = tk.Frame(lista_productos_window)
            frame.pack(padx=10, pady=10)

            # Crear una etiqueta para el encabezado
            tk.Label(frame, text="Listado de Productos").grid(row=0, columnspan=2, pady=10)

            # Crear una tabla para mostrar los productos
            for i, producto in enumerate(productos, start=1):
                tk.Label(frame, text=f"Producto {i}").grid(row=i, column=0, sticky='w')
                tk.Label(frame, text=f"ID: {producto[0]}").grid(row=i, column=1, sticky='w')
                tk.Label(frame, text=f"Nombre: {producto[1]}").grid(row=i, column=2, sticky='w')
                tk.Label(frame, text=f"Descripción: {producto[2]}").grid(row=i, column=3, sticky='w')
                tk.Label(frame, text=f"Precio: {producto[3]}").grid(row=i, column=4, sticky='w')
                tk.Label(frame, text=f"Stock: {producto[4]}").grid(row=i, column=5, sticky='w')

            lista_productos_window.mainloop()
        else:
            print("Error al cargar los productos")

    # Crear un botón para mostrar los productos
    listar_button = tk.Button(app, text="Listar Productos", command=mostrar_producto)
    listar_button.pack(padx=10, pady=10)