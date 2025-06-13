
from helpers.operaciones import frecuencia_digitos, suma_digitos, union_conjuntos, interseccion_conjuntos, diferencia_conjuntos, diferencia_simetrica_conjuntos, crear_conjunto_ordenado
from helpers.inputs import ingreso_lista_de_numeros

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

  print("Conjuntos ordenados")
  for conjunto in conjuntos.values():
    print(conjunto)


  union_conjuntos(conjuntos)
  interseccion_conjuntos(conjuntos)
  diferencia_conjuntos(conjuntos)
  diferencia_simetrica_conjuntos(conjuntos)

  for dni in numeros:
    frecuencia_digitos(dni)
  
  print("Suma de digitos")
  for dni in numeros:
    print(f"Dni: {dni}")
    print(suma_digitos(dni))

  print("Expresiones lógicas de conjuntos")
  if len(interseccion_conjuntos(conjuntos)) > 0:
    print("Digito Compartido")
  
  for conjunto in conjuntos.values():
    if len(conjunto) > 6:
      print('Diversidad numerica alta')

operaciones_conjuntos()