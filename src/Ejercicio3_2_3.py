'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar 
un mensaje informando de ello.

Fruta 	    Precio
Plátano 	1.35
Manzana 	0.80
Pera 	    0.85
Naranja 	0.70
'''

def diccionario():

    precioFruta ={'Plátano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
    return precioFruta

def leerEntrada():

    fruta = input("Que fruta quieres: ")
    kilos = int(input("Cuantos quilos quieres: "))
    return fruta,kilos

def checkDiccionario(fruta,precioFruta):

    if fruta in precioFruta:
        return True
    else:
        return False

def kilosFrutas(kilos,fruta,precioFruta):
    if checkDiccionario(fruta, precioFruta):
        precioTotal = kilos * precioFruta[fruta]
        return precioTotal
    else:
        return None

def mostrarMensaje(fruta,kilos,precioTotal):
    if precioTotal is not None:
        return f"El precio total de {kilos} kilos de {fruta} es {precioTotal} euros."
    
def procesarEntrada():
    fruta, kilos = leerEntrada()
    precioFruta = diccionario()

    if checkDiccionario(fruta, precioFruta):
        precioTotal = kilosFrutas(kilos, fruta, precioFruta)
        print(mostrarMensaje(fruta, kilos, precioTotal))
    else:
       print("Lo siento, esa fruta no está en el diccionario de precios.")
    
if __name__ == "__main__":
     procesarEntrada()
    
