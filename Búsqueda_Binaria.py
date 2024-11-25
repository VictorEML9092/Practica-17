"""
Created on Monday 25/11/24

@author: Victor Mendoza
"""

def busqueda_binaria(lista):
    print("\nLa lista es:", lista)
    objetivo = int(input("\nIngrese el número que desea buscar: "))
    
    inicio = 0
    fin = len(lista) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(f"\n{medio} = ({inicio} + {fin}) // 2")
        if lista[medio] == objetivo:
            print(f"\n{lista[medio]} == {objetivo}")
            print(f"\nElemento encontrado en el índice {medio}")
            encontrado = True
            break
        elif lista[medio] < objetivo:
            print(f"\n{medio} < {objetivo}")
            inicio = medio + 1
            print(f"\n{inicio} = {medio} + 1")
        else:
            print(f"\n{fin} = {medio} - 1")
            fin = medio - 1

    if not encontrado:
        print("\nElemento no encontrado")

    # Preguntar si se desea buscar otro número
    resp = input("\n¿Desea buscar otro número? (Si/No): ").strip().lower()
    if resp == "si":
        busqueda_binaria(lista)

# Ejemplo de uso
lista = []

cantidad = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))

for i in range(cantidad):
    elemento = int(input("\nIngrese un número: "))
    lista.append(elemento)

lista.sort()  # La lista debe estar ordenada para la búsqueda binaria

busqueda_binaria(lista)