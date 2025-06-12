import math

# Desarrollo del archivo .py simple y explicativo para el Trabajo Integrador 2 
# Definimos funciones claras y bien documentadas para cada parte solicitada 

# 1. Función para obtener conjunto de dígitos únicos a partir del DNI 
def obtener_conjunto_digitos(dni): 
    #Inicializamos un conjunto vacío para almacenar dígitos únicos
    digitos_dni = set()
    #Recorremos el DNI ingresado
    for digito in dni:
        #Evaluamos si es un digito númerico
        if digito.isdigit():
            #Ingresamos el valor dentro del conjunto  
            digitos_dni.add(int(digito))
            #Devolvemos el conjunto con valores unicos. 
    return digitos_dni

# Solicitamos los DNI
dni_1 = input("Ingrese primer DNI sin puntos :")
dni_2 = input("Ingrese segundo DNI, sin puntos:")

# Armamos los conjuntos y los guardamos en una variaable para utilizarlos durante el resto del programa.
conjunto_1 = obtener_conjunto_digitos(dni_1)
conjunto_2 = obtener_conjunto_digitos(dni_2)

# 1. Imprimos los conjuntos 
print(f"El primer conjunto de números es: {conjunto_1}")
print(f"El segundo conjunto de números es: {conjunto_2}")

# 2. Creamos una función para agrupar todos los calculos y visualizaciones, aprovechando los conjuntos creados. 
def operaciones_conjuntos(conjuntoA, conjuntoB):
    union = conjuntoA.union(conjuntoB)
    interseccion = conjuntoA & conjuntoB
    diferencia_1_2 = conjuntoA - conjuntoB
    diferencia_2_1 = conjuntoB - conjuntoA
    diferencia_simetrica = conjuntoA ^ conjuntoB

    return [union, interseccion, diferencia_1_2, diferencia_2_1, diferencia_simetrica]

# Hacemos uso de la función e imprimimos sus resultados. 
operaciones = operaciones_conjuntos(conjunto_1, conjunto_2)

# Imprimimos los resultados correspondientes
print("Unión:", operaciones[0])
print("Intersección:", operaciones[1])
print("Diferencia (1 - 2):", operaciones[2])
print("Diferencia (2 - 1):", operaciones[3])
print("Diferencia Simétrica:", operaciones[4])

# 3. Identificamos la frecuencia de cada digito en el DNI. 
def resumen_frecuencia_digitos(dni):
    print(f"Frecuencia de digitos para el DNI {dni}:\n")

    # Recorremos los digitos posibles del 0 al 9 como caracteres
    for numero in "0123456789":
        contador = 0
        # Recorremos el DNI caracter por caracter
        for caracter in dni:
            if caracter == numero:
                contador += 1
        # Solo mostramos si el dígito aparece al menos una vez
        if contador > 0:
            print(f"Dígito {numero}: {contador} {'vez' if contador == 1 else 'veces'}")

# Imprimimos la frecuencia para cada DNI
resumen_frecuencia_digitos(dni_1)
resumen_frecuencia_digitos(dni_2)

# 4. Suma de los dígitos 
def suma_digitos(dni):
    suma = 0
    for digito in dni:
        if digito.isdigit():
            suma += int(digito)
    return suma

print(f"La suma total del {dni_1} es {suma_digitos(dni_1)}")
print(f"La suma total del {dni_2} es {suma_digitos(dni_2)}")

# 5. Evaluamos condicones lógicas. 
def evaluar_condiciones_logicas(conjuntoA, conjuntoB):
    # Usamos la función que ya tienes para obtener operaciones
    resultados = operaciones_conjuntos(conjuntoA, conjuntoB)

    # 1. Dígitos que aparecen en ambos conjuntos (intersección)
    digitos_compartidos = operaciones[1]
    if digitos_compartidos:
        print("Dígito(s) compartido(s):", ", ".join(str(d) for d in sorted(digitos_compartidos)))

    # 2. Evaluar si algún conjunto tiene más de 6 elementos
    if len(conjuntoA) > 6:
        print(f"Diversidad numérica alta en conjunto 1 (tiene {len(conjuntoA)} elementos)")
    if len(conjuntoB) > 6:
        print(f"Diversidad numérica alta en conjunto 2 (tiene {len(conjuntoB)} elementos)")

# Imprimimos condiciones evaluadas. 
evaluar_condiciones_logicas(conjunto_1, conjunto_2)
