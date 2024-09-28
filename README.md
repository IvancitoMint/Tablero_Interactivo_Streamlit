# Tablero_Interactivo_Streamlit
Un tablero interactivo utilizando Streamlit que integra 10 ejercicios sobre funciones en Python. El objetivo es poder crear una aplicación web simple donde los usuarios puedan ingresar datos, y las funciones resuelvan y muestren el resultado de cada ejercicio de manera interactiva.
Este reporte describe dos códigos de un programa que utiliza Streamlit para proporcionar diferentes funcionalidades. 

## Interfaz de Usuario con Streamlit

### Importaciones
```python
import streamlit as st
from funciones import *
```
- Descripción: Importa la biblioteca streamlit para crear la interfaz de usuario y las funciones definidas en el segundo código.

### Opciones del menú
```python
menu_opciones = ["Página principal", "Saludo simple", "Suma de dos números", "Área de un triangulo", 
                 "Calculadora de descuento", "Suma de una lista de números", "Producto con valores predeterminados", 
                 "Números pares e impares", "Multiplicación con *args", 
                 "Información de una persona con **kwargs", "Calculadora flexible"]
selected_option = st.sidebar.selectbox("Opciones", menu_opciones)
```
- Descripción: Define las opciones del menú que el usuario puede seleccionar y muestra un menú lateral.
### Estructura de Control match
```python
match selected_option:
```
- Descripción: Utiliza match para ejecutar diferentes bloques de código según la opción seleccionada por el usuario.
### Caso: Página Principal
```python
case "Página principal":
    st.title("Bienvenidos a mi página de funciones")
    st.markdown("#### Gonzalez Ochoa Ivan Alejandro")
    st.markdown("#### Facultad de ingeniería Mecánica y Eléctrica\n#### Ingeniería en Computación Inteligente 3B")
```
- Descripción: Muestra un título y una breve presentación sobre mí.
### Caso: Saludo Simple
```python
case "Saludo simple":
    st.title("Bienvenidos a la función de saludo")
    name = st.text_input("Escribe tu nombre:")
    if name:
        st.write(saludar(name))
```
- Descripción: Permite al usuario ingresar su nombre y muestra un saludo utilizando la función saludar.
### Caso: Suma de Dos Números
```python
case "Suma de dos números":
    st.title("Bienvenidos a la función suma de dos números")
    x = st.number_input("Ingrese el primer número:", step=1.00, format="%.2f")
    y = st.number_input("Ingrese el segundo número:", step=1.00, format="%.2f")
    if x or y:
        st.write(sumar(x, y))
```
- Descripción: Solicita dos números y muestra su suma utilizando la función sumar.
### Caso: Área de un Triángulo
```python
case "Área de un triangulo":
    base:float = st.number_input("Ingrese la base del triangulo", min_value=1.00, step=1.00,format="%.2f")
        altura:float = st.number_input("Ingrese la altura del triangulo", min_value=1.00, step=1.00,format="%.2f")
        st.write(calcula_area_triangulo(base,altura))
```
- Descripción: Permite al usuario ingresar la base y la altura de un triángulo y muestra su área utilizando la función calcula_area_triangulo.
### Caso: Calculadora de Descuento
```python
case "Calculadora de descuento":
    opciones = ["Porcentajes predeterminado", "Porcentajes personalizados"]

        precio:float = st.number_input("Ingrese el precio original del producto", min_value=1.00, step=1.00,format="%.2f")
        st.write("Porcentaje de descuento: 10%")
        st.write("Porcentaje de impuestos: 16%")
        option = st.selectbox("Seleccione una opción", opciones)
        mensaje = st.empty() # Contenedor vacío
        match option:
            case "Porcentajes predeterminado":
                    mensaje.write(f"El precio final con descuento e impuesto es de: {calcular_precio_final(precio)}")
            case "Porcentajes personalizados":
                descuento:float = st.number_input("Ingrese el porcentaje del descuento", min_value=0.00, step=1.00,format="%.2f")
                impuesto:float = st.number_input("Ingrese el porcentaje del impuesto", min_value=0.00, step=1.00,format="%.2f")
                mensaje.write(f"El precio final con descuento e impuesto es de: {calcular_precio_final(precio,descuento,impuesto): .2f}")
```
- Descripción: Permite al usuario calcular el precio final de un producto considerando un descuento y un impuesto fijo o personalizado según lo que el usuario decida, esto utilizando la función calcular_precio_final.
- 
### Caso: Suma de una Lista de Números
```python
case "Suma de una lista de números":
    entrada = st.text_input("Ingresa los números separados por comas:")
            if entrada: # Procesamos la entrada solo si no está vacía
                try:
                    # Convertimos la cadena de texto en una lista de números y mostramos el resultado
                    lista_numeros = [float(num) for num in entrada.split(",")]
                    st.write(f"Números ingresados: {lista_numeros}")
                    st.write(f"La suma de los números es: {sumar_lista(lista_numeros)}") 
                except ValueError:
                    st.error("Por favor, ingresa solo números separados por comas.")
```
- Descripción: Permite al usuario ingresar una lista de números y muestra la suma utilizando la función sumar_lista.
### Caso: Producto con Valores Predeterminados
```python
case "Producto con valores predeterminados":
    opciones = ["Valores predeterminados", "Valores personalizados"]
    
            name = st.text_input("Ingresa el nombre del producto:")
            st.write("Cantidad de producto: 1")
            st.write("Precio del producto: $1")
            option = st.selectbox("Seleccione una opción", opciones)
            mensaje = st.empty() # Contenedor vacío
            match option:
                case "Valores predeterminados":
                        mensaje.write(f"El total a pagar por {name} es de: $1")
                case "Valores personalizados":
                    precio:float = st.number_input("Ingrese el precio del producto", min_value=1.00, step=1.00,format="%.2f")
                    cantidad:float = st.number_input("Ingrese la cantidad de producto", min_value=1.00, step=1.00,format="%.0f")
                    mensaje.write(f"El total a pagar por {name} es de: ${producto(precio,cantidad): .2f}")
```
- Descripción: Permite calcular el total a pagar por un producto considerando una cantidad y un precio fijo o variables, utilizando la función producto.
### Caso: Números Pares e Impares
```python
case "Números pares e imprares":
    entrada = st.text_input("Ingresa los números separados por comas:")
            if entrada: # Procesamos la entrada solo si no está vacía
                try:
                    # Convertimos la cadena de texto en una lista de números y mostramos resultados
                    lista_numeros = [float(num) for num in entrada.split(",")]
                    st.write(f"Números ingresados: {lista_numeros}")
                    pares, impares = numeros_pares_e_impares(lista_numeros)
                    st.write(f"Los números pares son: {pares}")
                    st.write(f"Los números impares son: {impares}")                
                except ValueError:
                    st.error("Por favor, ingresa solo números separados por comas.")
```
- Descripción: Muestra la lista de números ingresados y separa los pares de los impares en dos listas distintas utilizando la función numeros_pares_e_impares.
### Caso: Multiplicación con *args
```python
case "Multiplicación con *args":
    entrada = st.text_input("Ingresa los números separados por comas:")
            if entrada: # Procesamos la entrada solo si no está vacía
                try:
                    # Convertimos la cadena de texto en una lista de números y mostramos el resultado
                    lista_numeros = [float(num) for num in entrada.split(",")]
                    st.write(f"Números ingresados: {lista_numeros}")
                    st.write(f"El producto de los números es: {multiplicar_todos(*lista_numeros)}")              
                except ValueError:
                    st.error("Por favor, ingresa solo números separados por comas.")
```
- Descripción: Permite ingresar una lista de números y mostrarlos como una lista para depues mostrar su producto utilizando la función multiplicar_todos.
### Caso: Información de una Persona con **kwargs
```python
case "Información de una persona con **kwargs":
    mi_diccionario = {}
            numero_datos = st.number_input("Ingresa el número de datos a leer: ", step=1, min_value=1, format="%d")        
    
            for i in range(1, numero_datos + 1): # Para cada entrada, creamos inputs de texto para la clave y el valor
                clave = st.text_input(f"Ingresa la clave {i}:", key=f"clave_{i}")
                valor = st.text_input(f"Ingresa el valor {i}:", key=f"valor_{i}")
                if clave and valor: # Si ambos clave y valor están presentes, los añadimos al diccionario
                    mi_diccionario[clave] = valor
            if st.button("Imprimir los valores"): # Cuando el usuario haga clic en el botón, mostramos la información
                if mi_diccionario:
                    informacion_personal(**mi_diccionario)
                else:
                    st.error("Por favor, ingresa todos los pares clave-valor.")
```
- Descripción: Permite ingresar pares clave-valor primero preguntando cuantos elementos desea ingresar y el numero que elija será el numero de text_input que aparecerán para cada clave y valor, depues ambos datos se ingresan en un diccionario para despues enviarlos a la función informacion_personal y mostrar la información introduzida como clave-valor.
### Caso: Calculadora Flexible
```python
case "Calculadora flexible":
    opciones = ["Suma", "Resta", "Multiplicación", "División"]
            
            n1 = st.number_input("Ingresa el número uno", step=1.00,format="%.2f")
            n2 = st.number_input("Ingresa el número dos", step=1.00,format="%.2f")
            opc = st.selectbox("Seleccione una opción", opciones)
            if True:
                try:
                    st.write(calculadora_flexible(opc,n1,n2))
                except ValueError:
                    st.error("Por favor, ingresa solo números.")
```
- Descripción: Permite realizar operaciones básicas (suma, resta, multiplicación, división) entre dos números utilizando la función calculadora_flexible.
