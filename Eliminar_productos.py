from Conectar import conectar_eliminar
import tkinter as tk


def eliminar_productos():
    # Crear la ventana principal
    app = tk.Tk()
    app.title("Eliminación de Productos")

    # Crear un marco para organizar los elementos
    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    # Crear etiquetas y campo de entrada para ID
    tk.Label(frame, text="ID:").grid(row=0, column=0, sticky='w')
    id_entry = tk.Entry(frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    

    def eliminar_producto():
        # Obtener el valor del ID de entrada
        id_producto = id_entry.get()

        if not id_producto:
            print("Debe ingresar un ID válido.")
            return

        # Llama a la función Conectar para eliminar el producto de la base de datos
        resultado = conectar_eliminar(id_producto)

        if resultado:
            limpiar_entradas()
            print("Producto eliminado")
        else:
            print("Error al eliminar el producto")

    def limpiar_entradas():
        id_entry.delete(0, 'end')
        
    # Crear botón para eliminar el producto
    eliminar_button = tk.Button(frame, text="Eliminar Producto", command=eliminar_producto)
    eliminar_button.grid(row=1, columnspan=2, pady=10)
