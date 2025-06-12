# B. Operaciones con años de nacimiento

integrantes = int(input("Ingrese el número de intengrantes :"))
anios_nacimiento = []
for i in range(integrantes):
    while True:
        anio = int(input(f"Ingrese el año de nacimiento del integrante {i + 1}: "))
        if anio in anios_nacimiento:
            print("Ese año ya fue ingresado. Por favor, ingrese un año distinto (puede usar uno ficticio).")
        else:
            anios_nacimiento.append(anio)
            break

def anios_pares(lista):
    pares =0
    impares =0
    for anios in lista:
        if anios % 2 == 0: 
            pares += 1
        else:
            impares += 1
    print(f"Años pares: {pares}")
    print(f"Años impares: {impares}")

anios_pares(anios_nacimiento)
