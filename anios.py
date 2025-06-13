from helpers.conjuntos import union_conjuntos, interseccion_conjuntos, diferencia_conjuntos, diferencia_simetrica_conjuntos, frecuencias_digitos, crear_conjunto_ordenado, producto_cartesiano
from helpers.inputs import ingreso_lista_de_numeros
from helpers.date import es_par, es_bisiesto, es_generacion_z, obtener_edad_actual

def operaciones_conjuntos():
  # definicion de variables necesarias
  numeros = []
  conjuntos = {}
  # ingreso de números
  
  numeros = ingreso_lista_de_numeros("Ingresa un numero: ", "x")
  print("Numeros ingresados:", numeros)

  # Crear conjuntos ordenados a partir de los números ingresados
  for index, dni in enumerate(numeros):
    conjuntos[index + 1] = crear_conjunto_ordenado(dni)

  print("Conjuntos ordenados", conjuntos)

  interseccion_conjuntos(conjuntos)
  union_conjuntos(conjuntos) 
  diferencia_conjuntos(conjuntos)
  diferencia_simetrica_conjuntos(conjuntos)
  frecuencias_digitos(numeros)

def operaciones_anios():
  # ingreso de datos
  anios = ingreso_lista_de_numeros("Ingresa los años de nacimiento: ", "x")

  # variables auxiliares
  anios_par = 0
  grupo_z = True
  anio_especial = False
  edades_actuales = []

  # Iteración de datos ingresados para recolectar información
  for anio in anios:
    # par impar
    if es_par(anio):
      anios_par += 1

    if not es_generacion_z(anio):
      grupo_z = False

    if es_bisiesto(anio):
      anio_especial = True

    edades_actuales.append(obtener_edad_actual(anio))

  print("Información sobre años ingresados")

  print("Cantidad de pares e impares")
  print(f"Par: {anios_par}")
  print(f"Impar: {len(anios) - anios_par}")

  # Grupo z
  if grupo_z:
    print("Grupo Z")

  # Año bisiesto
  if anio_especial:
    print("Tenemos un año especial")
  
  print("Producto cartesiano entre años ingresados y edades actuales:")
  print(producto_cartesiano(anios, edades_actuales))
  
#operaciones_anios()
operaciones_conjuntos()