from producto import Producto
from Conectar import conectar_agregar
import tkinter as tk

# Función para abrir el componente de Agregar Productos
def agregar_productos():
    # Crear una ventana para agregar productos
    add_product_window = tk.Toplevel()
    add_product_window.title("Victor")
    add_product_window.geometry("400x200")

    # Crear etiquetas y campos de entrada para Nombre, Descripción, Precio y Stock
    tk.Label(add_product_window, text="Nombre:").pack()
    nombre_entry = tk.Entry(add_product_window)
    nombre_entry.pack()

    tk.Label(add_product_window, text="Descripción:").pack()
    descripcion_entry = tk.Entry(add_product_window)
    descripcion_entry.pack()

    tk.Label(add_product_window, text="Precio:").pack()
    precio_entry = tk.Entry(add_product_window)
    precio_entry.pack()

    tk.Label(add_product_window, text="Stock:").pack()
    stock_entry = tk.Entry(add_product_window)
    stock_entry.pack()

    # Función para agregar el producto
    def agregar_producto():
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get()
        precio = precio_entry.get()
        stock = stock_entry.get()

        # Aquí puedes agregar la lógica para guardar el producto en tu base de datos o en una lista, por ejemplo.
        roducto = Producto(nombre, descripcion, precio, stock)
        # Llama a la función Conectar para agregar el producto a la base de datos
        resultado = conectar_agregar(nombre, descripcion, precio, stock)        
        
        if resultado:
            limpiar_entradas()
            print("Producto agregado con éxito")
        else:
            print("Error al agregar el producto")
                # P ahora, solo imprimimos los valores.
        print("Nombre:", nombre)
        print("Descripción:", descripcion)
        print("Precio:", precio)
        print("Stock:", stock)
        
    def limpiar_entradas():
        nombre_entry.delete(0, 'end')
        descripcion_entry.delete(0, 'end')
        precio_entry.delete(0, 'end')
        stock_entry.delete(0, 'end')

        

    # Crear un botón para agregar el producto
    agregar_button = tk.Button(add_product_window, text="Agregar Producto", command=agregar_producto)
    agregar_button.pack()
