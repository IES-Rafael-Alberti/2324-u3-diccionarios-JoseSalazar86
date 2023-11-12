'''
Ejercicio 3.2.6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''
def leeEntrada():
    try:
        nombre = input("Introduce el nombre: ")
        edad = int(input("Introduce la edad: "))
        sexo = input("Introduce el sexo: ")
        telefono = input("Introduce el telefono: ")
        email = input("Introduce el correo: ")

        if not nombre.isalpha():
            raise ValueError("El nombre no debe contener números.")
        if edad < 0:
            raise ValueError("No has introducido un número válido para la edad.")
        if not sexo.isalpha():
            raise ValueError("El sexo no debe contener números.")
        if len(telefono) != 9 or not telefono.isdigit():
            raise ValueError("El número de teléfono no es válido. Debe tener exactamente 9 dígitos y no contener caracteres no numéricos.")
        # Verificar el formato del correo electrónico
        if "@" not in email or "." not in email:
            raise ValueError("El correo electrónico no tiene un formato válido.")
        
        return nombre, edad, sexo, telefono, email

    except ValueError as e:
        print(e)
        return None  # Devuelve None en caso de error

def main():
    diccionarioPersona = {}
    continuar = True

    while continuar:
        entrada = leeEntrada()

        if entrada is not None:
            diccionarioPersona = {
                'Nombre': entrada[0],
                'Edad': entrada[1],
                'Sexo': entrada[2],
                'Telefono': entrada[3],
                'Correo Electronico': entrada[4]
            }

            print("Contenido del diccionario:", diccionarioPersona)

            añadir = input("¿Quieres añadir más información? (s/n): ")
            if añadir.lower() != 's':
                continuar = False
def mostrarMensaje(diccionario):
    if diccionario:
        print("Contenido del diccionario:", diccionario)
    else:
        print("No se pudo procesar la entrada debido a errores.")
        
if __name__ == "__main__":
    main()

