#Erika Ivana Salinas Juarez
#Ing. TI 
from formas import Punto
from formas import Rectangulo
from formas import Elipse
from formas import Cuadrado
from formas import Circulo


print("PRUEBA DE LAS FORMAS")
print()


# Rectangulo

p1 = Punto(2, 3)

rectangulo = Rectangulo(
    "Rojo",
    p1,
    "Rectangulo 1",
    4,
    8
)

rectangulo.imprimir()

print("Area:", rectangulo.area())
print("Perimetro:", rectangulo.perimetro())

print()

rectangulo.cambiar_tamano(2)

print("Despues de cambiar el tamaño:")
print("Area:", rectangulo.area())
print("Perimetro:", rectangulo.perimetro())

print()


# Elipse

p2 = Punto(5, 5)

elipse = Elipse(
    "Verde",
    p2,
    "Elipse 1",
    6,
    3
)

elipse.imprimir()

print("Area:", elipse.area())
print("Perimetro:", elipse.perimetro())

print()


# Cuadrado

p3 = Punto(10, 10)

cuadrado = Cuadrado(
    "Azul",
    p3,
    "Cuadrado 1",
    5
)

cuadrado.imprimir()

print("Area:", cuadrado.area())
print("Perimetro:", cuadrado.perimetro())

print()


# Circulo

p4 = Punto(0, 0)

circulo = Circulo(
    "Amarillo",
    p4,
    "Circulo 1",
    4
)

circulo.imprimir()

print("Area:", circulo.area())
print("Perimetro:", circulo.perimetro())

print()


# Lista de formas

formas = [
    rectangulo,
    elipse,
    cuadrado,
    circulo
]


# Cambiar color y mover todas las formas

for forma in formas:
    forma.set_color("Negro")
    forma.mover(20, 20)


print("FORMAS DESPUES DE LOS CAMBIOS")
print()

for forma in formas:
    forma.imprimir()
    print("Area:", forma.area())
    print("Perimetro:", forma.perimetro())
    print()


# Buscar la forma con mayor area

mayor = formas[0]

for forma in formas:

    if forma.area() > mayor.area():
        mayor = forma


print("FORMA CON MAYOR AREA")
mayor.imprimir()
print("Area:", mayor.area())

print()


# Prueba de getters y setters

print("PRUEBA DE GETTERS Y SETTERS")

print("Color:", circulo.get_color())

circulo.set_color("Morado")

print("Nuevo color:", circulo.get_color())

print("Radio:", circulo.get_radio_mayor())

circulo.set_radio_mayor(6)

print("Nuevo radio:", circulo.get_radio_mayor())

print()


# Mover una forma

print("CENTRO DEL CIRCULO")

circulo.get_centro().imprimir()

circulo.mover(30, 30)

print("Nuevo centro:")

circulo.get_centro().imprimir()

print()
print("Fin del programa")
