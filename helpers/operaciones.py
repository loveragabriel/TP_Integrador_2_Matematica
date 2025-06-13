
def crear_conjunto_ordenado(numeros):
    return sorted(set(numeros))

def union_conjuntos(conjuntos):
  union_conjuntos = set()
  for conjunto in conjuntos.values():
    union_conjuntos.update(conjunto)
  print("Unión de todos los conjuntos:", sorted(union_conjuntos))
  return sorted(union_conjuntos)

def interseccion_conjuntos(conjuntos):
  print("Intersección de conjuntos")
  if not conjuntos:
    print("No existen intersección")
  elif len(conjuntos) == 1:
    print(f"Solo existe un conjunto: {conjuntos[1]}")
  else:
    cantidad_conjuntos = len(conjuntos)
    interseccion = []
    for numero in conjuntos[1]:
      es_interseccion = False
      for i in range(2, cantidad_conjuntos + 1):
        if numero in conjuntos[i]:
          es_interseccion = True
        else:
          es_interseccion = False
      if es_interseccion: interseccion.append(numero)
    if len(interseccion) == 1:
      print(f"Dígito representativo del grupo: {interseccion[0]}")
    else:
      print(f"No hay dígito representativo en el grupo")

    if len(interseccion):
      print(interseccion)
    else:
      print("No hay elementos que coincidan")
  return interseccion

# nuevo conjunto que contiene únicamente los elementos que pertenecen al primer conjunto, pero no a los demás
def diferencia_conjuntos(conjuntos):
  print("Diferencia entre conjuntos")
  if not conjuntos:
    print("No existen conjuntos")
  elif len(conjuntos) == 1:
    print(f"Solo existe un conjunto: {conjuntos[1]}")
  else:
    diferencia = []
    cantidad_conjuntos = len(conjuntos)
    for numero in conjuntos[1]:
      numero_existe = False
      for i in range(2, cantidad_conjuntos + 1):
        if numero in conjuntos[i]:
          numero_existe = True
      if not numero_existe: diferencia.append(numero)
    if len(diferencia):
      print(diferencia)
    else:
      print("No existe diferencia entre los elementos")

def diferencia_simetrica_conjuntos(conjuntos):
  print("Diferencia simétrica entre conjuntos:")
  # junto todos los conjuntos
  conjuntos_unidos = []
  for conjunto in conjuntos.values():
    conjuntos_unidos += conjunto
  # veo si se repiten
  valores_repetidos = {}
  for valor in conjuntos_unidos:
    if valor in valores_repetidos:
      valores_repetidos[valor] += 1
    else:
      valores_repetidos[valor] = 1
  
  # busco solo los que no se repiten
  conjunto_simetrico = []
  for valor in valores_repetidos.keys():
    if valores_repetidos[valor] == 1:
      conjunto_simetrico.append(valor)
  
  if len(conjunto_simetrico): print(conjunto_simetrico)
  else: print("No existe")

def frecuencia_digitos(dni):
  print(f"Frecuencia de digitos para el DNI {dni}:\n")

  # Recorremos los digitos posibles del 0 al 9 como caracteres
  for numero in range(0, 10):
    contador = 0
    # Recorremos el DNI caracter por caracter
    for caracter in dni:
      if int(caracter) == int(numero):
        contador += 1
    # Solo mostramos si el dígito aparece al menos una vez
    if contador > 0:
      print(f"Dígito {numero}: {contador} {'vez' if contador == 1 else 'veces'}")

def suma_digitos(dni):
    suma = 0
    for digito in dni:
        if digito.isdigit():
            suma += int(digito)
    return suma

def producto_cartesiano(conjunto1, conjunto2):
  producto_cartesiano = []
  
  for valor1 in sorted(conjunto1):
    for valor2 in sorted(conjunto2):
      producto_cartesiano.append([valor1, valor2])
  
  return producto_cartesiano
