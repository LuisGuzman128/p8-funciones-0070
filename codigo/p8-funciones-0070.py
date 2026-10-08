# UI Act 11 - Estructuras de datos y funciones
# Luis Axel Guzman Martinez
# NC 0070

# 1. Funcion basica
def saludo():
    print("Hola, bienvenido a Python")

saludo()


# 2. Funcion con parametro
def saludar(nombre):
    print("Hola", nombre)

saludar("Axel")


# 3. Funcion con dos parametros
def sumar(a, b):
    print("Resultado:", a + b)

sumar(10, 5)


# 4. Funcion con parametro
def mostrar_edad(edad):
    print("Edad:", edad)

mostrar_edad(15)


# 5. Parametro con valor por defecto
def saludo_default(nombre="Axel"):
    print("Hola", nombre)

saludo_default()


# 6. Dos parametros con valores por defecto
def sumar_default(a=5, b=3):
    print("Suma:", a + b)

sumar_default()


# 7. Parametro con valor por defecto
def pais(nombre="Mexico"):
    print("Pais:", nombre)

pais()


# 8. Funcion lambda
cuadrado = lambda x: x * x
print("Cuadrado:", cuadrado(5))


# 9. Recursividad
def contar(n):
    if n > 0:
        print(n)
        contar(n - 1)

contar(5)


# 10. Decorador
def decorador(funcion):
    def nueva_funcion():
        print("Inicio")
        funcion()
        print("Fin")
    return nueva_funcion


@decorador
def mensaje():
    print("Hola desde una funcion")

mensaje()
print("programa realizado por Axel Guzman 0070")