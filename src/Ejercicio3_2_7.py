'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
de la compra y el coste total, con el siguiente formato


Lista de la compra 	
Artículo 1 	Precio
Artículo 2 	Precio
Artículo 3 	Precio
… 	…
Total 	Coste
'''

def leerEntrada():
    articulo = input("Introduzca el producto: ")
    precio = float(input("Introduzca el precio: "))
    return articulo, precio

def mostrarListaCompra(cesta):
    print("\nLista de la compra")
    total = 0

    # Mostrar cada artículo y su precio
    for i, (articulo, precio) in enumerate(cesta.items(), start=1):
        print(f"Artículo {i}: {articulo}\tPrecio: {precio}")
        total += precio

    # Mostrar el coste total
    print(f"\nTotal\tCoste: {total}")

def main():
    cesta = {}  

    while True:
        # Leer entrada del usuario
        articulo, precio = leerEntrada()

        # Agregar el artículo y precio al diccionario
        cesta[articulo] = precio

        # Preguntar al usuario si quiere agregar más artículos
        respuesta = input("¿Quieres añadir otro artículo? (s/n): ")
        if respuesta.lower() != 's':
            break  # Salir del bucle si la respuesta no es 's'

    # Mostrar la lista de la compra y el coste total
    mostrarListaCompra(cesta)

if __name__ == "__main__":
    main()
