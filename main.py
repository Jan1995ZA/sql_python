from Agregar_productos import agregar_productos
from Eliminar_productos import eliminar_productos
from Mostrar_productos import mostrar_productos
from Modificar_productos import modificar_productos

import tkinter as tk
import tkinter.ttk as ttk

# Función para abrir una ventana emergente con un título dado
def open_window(title, component):
    window = tk.Toplevel()
    window.title(title)
    window.geometry("400x300")
    component(window)



# Crear la ventana principal
app = tk.Tk()
app.title("Gestión de Productos")
app.geometry("600x400")

# Crear un estilo para las etiquetas del encabezado
style = ttk.Style()
style.configure("Header.TLabel", font=("Arial", 14, "bold"))

# Crear un marco (frame) para organizar los elementos
frame = ttk.Frame(app)
frame.pack(expand=True, fill="both")

# Botones para las diferentes funcionalidades
listar_button = ttk.Button(frame, text="Listar Productos", command=lambda: mostrar_productos())
modificar_button = ttk.Button(frame, text="Modificar Productos", command=lambda: modificar_productos())
eliminar_button = ttk.Button(frame, text="Eliminar Productos", command=lambda: eliminar_productos())
agregar_button = ttk.Button(frame, text="Agregar Productos", command=lambda: agregar_productos())

# Colocar los botones en el marco con espaciado y estilo
listar_button.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="x")
modificar_button.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="x")
eliminar_button.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="x")
agregar_button.pack(pady=10, padx=20, ipadx=20, ipady=10, fill="x")

# Iniciar la aplicación principal
app.mainloop()
