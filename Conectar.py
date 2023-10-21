# database.py
import mysql.connector

def conectar_agregar(nombre, descripcion, precio, stock):
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            user='root',
            password='',  # Contraseña de tu base de datos
            host='localhost',
            database='panaderia',
            port=3306
        )

        cursor = conexion.cursor()

        # Consulta SQL para insertar el producto sin especificar el ID (se asignará automáticamente)
        insert_query = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
        values = (nombre, descripcion, precio, stock)

        cursor.execute(insert_query, values)
        conexion.commit()

        cursor.close()
        conexion.close()
        

        return True

    except mysql.connector.Error as error:
        print("Error al agregar el producto:", error)
        return False


def conectar_modificar(id_producto, nombre, descripcion, precio, stock):
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            user='root',
            password='',  # Contraseña de tu base de datos
            host='localhost',
            database='panaderia',
            port=3306
        )

        cursor = conexion.cursor()

        # Consulta SQL para actualizar el producto
        update_query = "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE id=%s"
        values = (nombre, descripcion, precio, stock, id_producto)

        cursor.execute(update_query, values)
        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except mysql.connector.Error as error:
        print("Error al modificar el producto:", error)
        return False
    
def conectar_eliminar(id_producto):
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            user='root',
            password='',  # Contraseña de tu base de datos
            host='localhost',
            database='panaderia',
            port=3306
        )

        cursor = conexion.cursor()

        # Consulta SQL para eliminar el producto por ID
        delete_query = "DELETE FROM productos WHERE id=%s"
        values = (id_producto,)

        cursor.execute(delete_query, values)
        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    except mysql.connector.Error as error:
        print("Error al eliminar el producto:", error)
        return False

def conectar_listar():
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            user='root',
            password='',  # Contraseña de tu base de datos
            host='localhost',
            database='panaderia',
            port=3306
        )

        cursor = conexion.cursor()

        # Consulta SQL para listar todos los productos
        select_query = "SELECT * FROM productos"
        cursor.execute(select_query)
        productos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return productos

    except mysql.connector.Error as error:
        print("Error al listar productos:", error)
        return None