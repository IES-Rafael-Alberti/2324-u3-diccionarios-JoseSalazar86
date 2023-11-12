'''
Ejercicio 3.2.5

Escribir un programa que almacene el diccionario con los créditos 
de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> t
iene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
'''

def creditoAsignatura():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    return asignaturas

def sumaCredito(asignaturas):
    sumaTotal = sum(asignaturas.values())
    return sumaTotal

def mostrarMensaje(asignaturas, sumaTotal):
    mensaje = "Créditos de cada asignatura:"
    for asignatura, creditos in asignaturas.items():
        mensaje += f"\n{asignatura} tiene {creditos} créditos."

    mensaje += f"\nEl número total de créditos del curso es: {sumaTotal}."
    return mensaje

if __name__ == "__main__":
    asignaturas = creditoAsignatura()
    total_creditos = sumaCredito(asignaturas)
    mensaje = mostrarMensaje(asignaturas, total_creditos)
    print(mensaje)
