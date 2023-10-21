class Producto:
    def __init__(self, nombre, descripcion, precio, stock):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    def __str__(self):
        return f"Producto: {self.__nombre}, Descripción: {self.__descripcion}, Precio: {self.__precio}, Stock: {self.__stock}"
