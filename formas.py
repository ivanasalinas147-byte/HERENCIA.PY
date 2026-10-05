#Erika Ivana Salinas Juarez
#Ing. TI 
import math
from abc import ABC, abstractmethod


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("(", self.x, ",", self.y, ")")

    def mover(self, x, y):
        self.x = x
        self.y = y


class Forma(ABC):

    def __init__(self, color, centro, nombre):
        self.__color = color
        self.__centro = centro
        self.__nombre = nombre

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_centro(self):
        return self.__centro

    def set_centro(self, centro):
        self.__centro = centro

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def imprimir(self):
        print("Nombre:", self.__nombre)
        print("Color:", self.__color)
        print("Centro:", end=" ")
        self.__centro.imprimir()

    def mover(self, x, y):
        self.__centro.mover(x, y)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Rectangulo(Forma):

    def __init__(self, color, centro, nombre, lado_menor, lado_mayor):
        super().__init__(color, centro, nombre)
        self.__lado_menor = lado_menor
        self.__lado_mayor = lado_mayor

    def get_lado_menor(self):
        return self.__lado_menor

    def set_lado_menor(self, lado):
        self.__lado_menor = lado

    def get_lado_mayor(self):
        return self.__lado_mayor

    def set_lado_mayor(self, lado):
        self.__lado_mayor = lado

    def imprimir(self):
        print("Rectangulo")
        super().imprimir()
        print("Lado menor:", self.__lado_menor)
        print("Lado mayor:", self.__lado_mayor)

    def area(self):
        return self.__lado_menor * self.__lado_mayor

    def perimetro(self):
        return 2 * self.__lado_menor + 2 * self.__lado_mayor

    def cambiar_tamano(self, factor):
        self.__lado_menor = self.__lado_menor * factor
        self.__lado_mayor = self.__lado_mayor * factor


class Elipse(Forma):

    def __init__(self, color, centro, nombre, radio_mayor, radio_menor):
        super().__init__(color, centro, nombre)
        self.__radio_mayor = radio_mayor
        self.__radio_menor = radio_menor

    def get_radio_mayor(self):
        return self.__radio_mayor

    def set_radio_mayor(self, radio):
        self.__radio_mayor = radio

    def get_radio_menor(self):
        return self.__radio_menor

    def set_radio_menor(self, radio):
        self.__radio_menor = radio

    def imprimir(self):
        print("Elipse")
        super().imprimir()
        print("Radio mayor:", self.__radio_mayor)
        print("Radio menor:", self.__radio_menor)

    def area(self):
        return math.pi * self.__radio_mayor * self.__radio_menor

    def perimetro(self):
        a = self.__radio_mayor
        b = self.__radio_menor

        return 2 * math.pi * math.sqrt((a ** 2 + b ** 2) / 2)


class Cuadrado(Rectangulo):

    def __init__(self, color, centro, nombre, lado):
        super().__init__(color, centro, nombre, lado, lado)

    def imprimir(self):
        print("Cuadrado")
        super().imprimir()


class Circulo(Elipse):

    def __init__(self, color, centro, nombre, radio):
        super().__init__(color, centro, nombre, radio, radio)

    def imprimir(self):
        print("Circulo")
        super().imprimir()

    def perimetro(self):
        return 2 * math.pi * self.get_radio_mayor()
