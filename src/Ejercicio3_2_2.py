'''
Ejercicio 3.2.2

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

def diccionario(nombre, edad, direccion, telefono):
    diccionarioVacio = {'Nombre': nombre, 'Edad': edad, 'Direccion': direccion, 'Telefono': telefono}
    return diccionarioVacio

def leerEntrada():
    try:
        nombre = input("Introduce tu nombre: ")
        edad = int(input("Introduce tu edad: "))
        direccion = input("Introduce tu direccion: ")
        telefono = input("Introduce tu telefono: ")

        if not nombre.isalpha():
            raise ValueError("El nombre no debe contener numeros")

        if edad < 0:
            raise ValueError("No has introducido un numero para la edad")

        if len(telefono) != 9 or not telefono.isdigit():
            raise ValueError("El número de teléfono no es válido. Debe tener exactamente 9 dígitos y no contener caracteres no numéricos.")
        
    except ValueError as e:
        print(e)
    return nombre, edad,direccion,telefono


def mostrarMensaje(nombre, edad, direccion, telefono):
    diccionarioVacio = diccionario(nombre, edad, direccion, telefono)
    mensaje = f"{diccionarioVacio['Nombre']} tiene {diccionarioVacio['Edad']} años, vive en {diccionarioVacio['Direccion']} y su número de teléfono es {diccionarioVacio['Telefono']}"
    return mensaje

if __name__ == "__main__":
     
    nombre, edad, direccion, telefono = leerEntrada()
    if nombre and edad and direccion and telefono:
        mensaje = mostrarMensaje(nombre, edad, direccion, telefono)
        print(mensaje)