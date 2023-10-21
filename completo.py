import tkinter as tk
from tkinter import messagebox

# Función para mostrar un mensaje de acerca de
def acerca_de():
    messagebox.showinfo("Acerca de", "Tu aplicación para gestionar productos")

# Función para abrir la ventana de registro de productos
def abrir_ventana_registro():
    ventana_principal.destroy()  # Cierra la ventana principal
    ventana_registro = tk.Tk()
    ventana_registro.title("Registro de Productos")
    # Llama a una función que crea y configura la ventana de registro
    configurar_ventana_registro(ventana_registro)
    ventana_registro.mainloop()

# Función para configurar la ventana de registro de productos
def configurar_ventana_registro(ventana):
    frame = tk.Frame(ventana)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky='w')
    nombre_entry = tk.Entry(frame)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Agregar más elementos de la ventana de registro aquí

    agregar_button = tk.Button(frame, text="Agregar Producto", command=agregar_producto)
    agregar_button.grid(row=4, columnspan=2, pady=10)

# Función para agregar un producto
def agregar_producto():
    # Agregar lógica para agregar un producto aquí
    pass

def main():
    # Crear la ventana principal
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Gestión de Productos")

    # Crear una barra de menú
    barra_menu = tk.Menu(ventana_principal)

    menu_productos = tk.Menu(barra_menu, tearoff=0)
    menu_productos.add_command(label="Agregar Producto", command=abrir_ventana_registro)
    # Agregar más opciones de menú para productos aquí

    barra_menu.add_cascade(label="Productos", menu=menu_productos)
    barra_menu.add_command(label="Acerca de", command=acerca_de)

    ventana_principal.config(menu=barra_menu)
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
