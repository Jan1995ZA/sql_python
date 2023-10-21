from producto import Producto
from Conectar import conectar_modificar
import tkinter as tk

# Función para abrir el componente de Agregar Productos
def modificar_productos():
    # Crear la ventana principal
    app = tk.Tk()
    app.title("Modificación de Productos")
    
    # Crear un marco para organizar los elementos
    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)
    
    # Crear etiquetas y campos de entrada para ID, Nombre, Descripción, Precio y Stock
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky='w')
    id_entry = tk.Entry(frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky='w')
    nombre_entry = tk.Entry(frame)
    nombre_entry.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(frame, text="Descripción:").grid(row=2, column=0, sticky='w')
    descripcion_entry = tk.Entry(frame)
    descripcion_entry.grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(frame, text="Precio:").grid(row=3, column=0, sticky='w')
    precio_entry = tk.Entry(frame)
    precio_entry.grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(frame, text="Stock:").grid(row=4, column=0, sticky='w')
    stock_entry = tk.Entry(frame)
    stock_entry.grid(row=4, column=1, padx=5, pady=5)

    # Función para agregar el producto
    def modificar_producto():
    # Obtener los valores de las entradas de texto
        id_producto = id_entry.get()
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get()
        precio = precio_entry.get()
        stock = stock_entry.get()

        # Llama a la función Conectar para modificar el producto en la base de datos
        resultado = conectar_modificar(id_producto, nombre, descripcion,precio,stock)
    
        if resultado:
            limpiar_entradas()
            print("Producto modificado")
        else:
            print("Error al modificar")
        
    def limpiar_entradas():
        nombre_entry.delete(0, 'end')
        descripcion_entry.delete(0, 'end')
        precio_entry.delete(0, 'end')
        stock_entry.delete(0, 'end')

        

    # Crear botón para modificar el producto
    modificar_button = tk.Button(frame, text="Modificar Producto", command=modificar_producto)
    modificar_button.grid(row=5, columnspan=2, pady=10)