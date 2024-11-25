"""
Created on Monday 25/11/24

@author: Victor Mendoza
"""

def busqueda_secuencial(lista):
    print("\nLa lista es:", lista)
    objetivo = int(input("\nIngrese el número que desea buscar: "))

    encontrado = False
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            print(f"\nElemento encontrado en el índice {i}")
            encontrado = True
            break

    if not encontrado:
        print("\nElemento no encontrado")

    # Preguntar si se desea buscar otro número
    resp = input("\n¿Desea buscar otro número? (Si/No): ").strip().lower()
    if resp == "si":
        busqueda_secuencial(lista)

# Ejemplo de uso
lista = []

cantidad = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))

for i in range(cantidad):
    elemento = int(input("\nIngrese un número: "))
    lista.append(elemento)

lista.sort()  # Ordenar la lista si es necesario (aunque no es obligatorio para búsqueda secuencial)

busqueda_secuencial(lista)