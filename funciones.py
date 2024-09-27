import streamlit as st

def saludar(name:str) -> str:
    return f"Hola {name}, Bienvenido a mi programa. :D"

def sumar(x:float,y:float) -> float:
    return f"La suma de los números es: {x+y}"

def calcula_area_triangulo(base:float,altura:float) -> float:
    return f"El area del traingulo es: {(base*altura) / 2}"

def calcular_precio_final(precio_original, descuento = 10, impuesto = 16) -> float:
    precio_descuento = precio_original - (precio_original * (descuento/100))
    return precio_descuento + (precio_descuento * (impuesto/100))

def sumar_lista(lista:list) -> float:
    s = 0
    for n in lista:
        s += n
    return s

def producto(nombre_producto = "", cantidad = 1, precio = 1) -> float:
    return cantidad * precio

def numeros_pares_e_impares(lista:list) -> list:
    lista_pares = []
    lista_impares = []

    for n in lista:
        if n%2 == 0:
            lista_pares.append(n)
        else:
            lista_impares.append(n)
    return lista_pares, lista_impares

def multiplicar_todos(*args) -> float:
    producto = 1
    for n in args:
        producto = producto * n
    return producto

def informacion_personal(**kwargs):
    for clave, valor in kwargs.items():
        st.write(f"{clave}: {valor}")

def calculadora_flexible(opc:str, n1:float, n2:float) -> str:
    match opc:
        case "Suma":
            return f"La suma es: {n1 + n2}"
        case "Resta":
            return f"La resta es: {n1 - n2}"
        case "Multiplicación":
            return f"La multiplicación es: {n1 * n2}"
        case "División":
            if n1 == 0 and n2 == 0:
                return f"La divisón es: 0"
            elif n2 == 0:
                st.error("ERROR. División entre cero.")
            else:
                return f"La divisón es: {n1 / n2}"