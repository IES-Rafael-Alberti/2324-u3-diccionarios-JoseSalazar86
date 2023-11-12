'''
Ejercicio 3.2.1

Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

def diccionario():
    diccionarioDivisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    return diccionarioDivisa

def leerEntrada():
    divisa = input("Introduce una divisa: ")
    return divisa

def checkDivisa(diccionarioDivisa):
    
    if divisa in diccionarioDivisa:
        return True
    else:
        return False

def mostrarMensaje(divisa):
    diccionarioDivisa = diccionario()
    if checkDivisa(diccionarioDivisa):
       print(f"El símbolo de {divisa} es {diccionarioDivisa[divisa]}")
    else:
        print("La divisa introducida no se encuentra")
    
if __name__ == "__main__":
    divisa = leerEntrada()
    mostrarMensaje(divisa)