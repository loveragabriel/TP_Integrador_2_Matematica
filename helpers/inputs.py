def ingreso_lista_de_numeros(mensaje, terminar):
  continuar = True
  datos = []
  while continuar:
    ingreso_numero = input(f"{mensaje} (o escriba {terminar} para terminar): ")
    if ingreso_numero.lower() == terminar:
      continuar = False
    else:
      try:
        datos.append(ingreso_numero)
      except ValueError:
        print("Por favor, ingrese un número válido.")
  
  if not len(datos):
    print("No se ingresaron datos")

  return datos
