import streamlit as st
from funciones import *

#Opciones del menu
menu_opciones = ["Página principal","Saludo simple", "Suma de dos números", "Área de un triangulo", "Calculadora de descuento",
                 "Suma de una lista de números", "Valores predeterminados", "Números pares e imprares", "Multiplicación con *args",
                 "Información de una persona con **kwargs", "Calculadora flexible"]
selected_option = st.sidebar.selectbox("Opciones", menu_opciones)

#Opcion seleccionada
match selected_option:
    case "Página principal":
        st.title("Bienvenidos a mi página de funciones")
        st.markdown("#### Gonzalez Ochoa Ivan Alejandro")
        st.markdown("#### Facultad de ingeniería Mecánica y Eléctrica\n#### Ingeniería en Computación Inteligente 3B")

    case "Saludo simple":
        st.title("Bienvenidos a la función de saludo")

        name = st.text_input("Escribe tu nombre:")
        if name:
            st.write(saludar(name))

    case "Suma de dos números":
        st.title("Bienvenidos a la función suma de dos números")

        x = st.number_input("Ingrese el primer número:", step=1.00,format="%.2f")
        y = st.number_input("Ingrese el segundo número:", step=1.00,format="%.2f")
        if x and y:
            st.write(sumar(x,y))

    case "Área de un triangulo":
        st.title("Bienvenidos a la función área de un triangulo")

        base = st.number_input("Ingrese la base del triangulo")
        altura = st.number_input("Ingrese la altura del triangulo")
        if base > 0 and altura > 0: #Verificamos que los valores sea válido
            st.write(calcula_area_triangulo(base,altura))

    case "Calculadora de descuento":
        st.title("Bienvenidos a la función calculadora de descuento")
        opciones = ["Porcentajes predeterminado", "Porcentajes personalizados"]

        precio = st.number_input("Ingrese el precio original del producto", step=1.00,format="%.2f")

        st.write("Porcentaje de descuento: 10%")
        st.write("Porcentaje de impuestos: 16%")
        option = st.selectbox("Seleccione una opción", opciones)
        mensaje = st.empty() #Contenedor vacío

        match option:
            case "Porcentajes predeterminado":
                if precio > 0: #Verificamos que el precio sea válido
                    mensaje.write(f"El precio final con descuento e impuesto es de: {calcular_precio_final(precio)}")
            case "Porcentajes personalizados":
                descuento = st.number_input("Ingrese el porcentaje del descuento", step=1.00,format="%.0f")
                impuesto = st.number_input("Ingrese el porcentaje del impuesto", step=1.00,format="%.0f")
                if precio > 0: #Verificamos que el precio sea válido
                    mensaje.write(f"El precio final con descuento e impuesto es de: {calcular_precio_final(precio,descuento,impuesto)}")

    case "Suma de una lista de números":
        st.title("Bienvenidos a la función suma de listas")
        
        entrada = st.text_input("Ingresa los números separados por comas:")
        if entrada: #Procesamos la entrada solo si no está vacía
            try:
                #Convertimos la cadena de texto en una lista de números y mostramos el resultado
                lista_numeros = [float(num) for num in entrada.split(",")]
                st.write(f"Números ingresados: {lista_numeros}")
                st.write(f"La suma de los números es: {sumar_lista(lista_numeros)}") 
            except ValueError:
                st.error("Por favor, ingresa solo números separados por comas.")

    case "Valores predeterminados":
        st.title("Bienvenidos a la función valores predeterminados")
        opciones = ["Valores predeterminado", "Valores personalizados"]

        name = st.text_input("Ingresa el nombre del producto:")
        st.write("Cantidad de producto: 1")
        st.write("Precio del producto: $1")
        option = st.selectbox("Seleccione una opción", opciones)
        mensaje = st.empty() #Contenedor vacío
        match option:
            case "Valores predeterminado":
                    mensaje.write(f"El total a pagar por {name} es de: ${producto(name)}")
            case "Valores personalizados":
                precio = st.number_input("Ingrese el precio del producto", step=1.00,format="%.2f")
                cantidad = st.number_input("Ingrese la cantidad de producto", step=1.00,format="%.0f")
                if precio > 0 and cantidad > 0: # Verificamos que el precio sea válido
                    mensaje.write(f"El total a pagar por {name} es de:: ${producto(name,precio,cantidad)}")

    case "Números pares e imprares":
        st.title("Bienvenidos a la función Números pares e imprares")
        
        entrada = st.text_input("Ingresa los números separados por comas:")
        if entrada: #Procesamos la entrada solo si no está vacía
            try:
                #Convertimos la cadena de texto en una lista de números y mostramos resultados
                lista_numeros = [float(num) for num in entrada.split(",")]
                st.write(f"Números ingresados: {lista_numeros}")
                pares, impares = numeros_pares_e_impares(lista_numeros)
                st.write(f"Los números pares son: {pares}")
                st.write(f"Los números impares son: {impares}")                
            except ValueError:
                st.error("Por favor, ingresa solo números separados por comas.")

    case "Multiplicación con *args":
        st.title("Bienvenidos a la función Multiplicación con *args")
        
        entrada = st.text_input("Ingresa los números separados por comas:")
        if entrada: # Procesamos la entrada solo si no está vacía
            try:
                # Convertimos la cadena de texto en una lista de números y mostramos el resultado
                lista_numeros = [float(num) for num in entrada.split(",")]
                st.write(f"Números ingresados: {lista_numeros}")
                st.write(f"El producto de los números es: {multiplicar_todos(*lista_numeros)}")              
            except ValueError:
                st.error("Por favor, ingresa solo números separados por comas.")

    case "Información de una persona con **kwargs":
        st.title("Bienvenidos a la función Información de una persona con **kwargs")
        mi_diccionario = {}
        numero_datos = st.number_input("Ingresa el número de datos a leer: ", step=1, min_value=1, format="%d")        

        # Para cada entrada, creamos inputs de texto para la clave y el valor
        for i in range(1, numero_datos + 1):
            clave = st.text_input(f"Ingresa la clave {i}:", key=f"clave_{i}")
            valor = st.text_input(f"Ingresa el valor {i}:", key=f"valor_{i}")
            if clave and valor: #Si ambos clave y valor están presentes, los añadimos al diccionario
                mi_diccionario[clave] = valor

        if st.button("Imprimir los valores"): # Cuando el usuario haga clic en el botón, mostramos la información
            if mi_diccionario:
                informacion_personal(**mi_diccionario)
            else:
                st.error("Por favor, ingresa todos los pares clave-valor.")

    case "Calculadora flexible":
        st.title("Bienvenidos a la función Calculadora flexible")
        opciones = ["Suma", "Resta", "Multiplicación", "División"]
        
        n1 = st.number_input("Ingresa el número uno", step=1.00,format="%.2f")
        n2 = st.number_input("Ingresa el número dos", step=1.00,format="%.2f")
        opc = st.selectbox("Seleccione una opción", opciones)
        if True:
            try:
                st.write(calculadora_flexible(opc,n1,n2))
            except ValueError:
                st.error("Por favor, ingresa solo números.")