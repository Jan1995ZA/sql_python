
from producto import Producto
from Conectar import conectar
import tkinter as tk
def agregar_producto():
    # Obtener los valores de las entradas de texto
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get()
    precio = precio_entry.get()
    stock = stock_entry.get()
    
    producto = Producto(nombre, descripcion, precio, stock)
    
    # Llama a la función Conectar para agregar el producto a la base de datos
    resultado = conectar(nombre, descripcion, precio, stock)
    
    
    if resultado:
        limpiar_entradas()
        print("Producto agregado con éxito")
    else:
        print("Error al agregar el producto")


def limpiar_entradas():
    nombre_entry.delete(0, 'end')
    descripcion_entry.delete(0, 'end')
    precio_entry.delete(0, 'end')
    stock_entry.delete(0, 'end')


# Crear la ventana principal
app = tk.Tk()
app.title("Registro de Productos")

# Crear un marco para organizar los elementos
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# Crear etiquetas y campos de entrada para Nombre, Descripción, Precio y Stock
tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w')
nombre_entry = tk.Entry(frame)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Descripción:").grid(row=1, column=0, sticky='w')
descripcion_entry = tk.Entry(frame)
descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Precio:").grid(row=2, column=0, sticky='w')
precio_entry = tk.Entry(frame)
precio_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Stock:").grid(row=3, column=0, sticky='w')
stock_entry = tk.Entry(frame)
stock_entry.grid(row=3, column=1, padx=5, pady=5)

# Crear botón para agregar el producto
agregar_button = tk.Button(frame, text="Agregar Producto", command=agregar_producto)
agregar_button.grid(row=4, columnspan=2, pady=10)

# Iniciar la aplicación
app.mainloop()
