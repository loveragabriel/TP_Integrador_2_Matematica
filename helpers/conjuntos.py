
def crear_conjunto_ordenado(numeros):
    return sorted(set(numeros))

def union_conjuntos(conjuntos):
  union_conjuntos = set()
  for conjunto in conjuntos.values():
    union_conjuntos.update(conjunto)
  print("Unión de todos los conjuntos:", sorted(union_conjuntos))

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

    if len(interseccion):
      print(interseccion)
    else:
      print("No hay elementos que coincidan")

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

def frecuencias_digitos(numeros):
  print("Freciencias de dígitos en numeros ingresados")
  frecuencias = {}
  
  for numero in numeros:
    for digito in numero:
      if numero in frecuencias:
        if digito in frecuencias[numero]:
          frecuencias[numero][digito] += 1
        else:
          frecuencias.update(numero)
  print(frecuencias)
  
def producto_cartesiano(conjunto1, conjunto2):
  producto_cartesiano = []
  
  for valor1 in sorted(conjunto1):
    for valor2 in sorted(conjunto2):
      producto_cartesiano.append([valor1, valor2])
  
  return producto_cartesiano