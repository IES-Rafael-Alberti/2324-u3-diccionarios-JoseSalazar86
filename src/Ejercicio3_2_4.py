'''
Ejercicio 3.2.4¶

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes>
es el nombre del mes.
'''
def leerEntrada():

    year = input("Introduce la fecha en formato dd/mm/aaaa: ")

    return year

def convertirFecha(fecha):
    dia, mes,year = map(int,fecha.split('/'))

    meses ={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',
            7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',
            12:'Diciembre'}
    nombreDelMes = meses.get(mes, 'Mes inválido')
    
    return dia, nombreDelMes, year

def mostrarMensaje(dia,nombreDelMes,year):
    fechaNueva = f"{dia} de {nombreDelMes} de {year}"
    return fechaNueva

def main():
    fecha = leerEntrada()

    dia, nombreDelMes, year = convertirFecha(fecha)

    mensaje = mostrarMensaje(dia,nombreDelMes,year)
    print(mensaje)

if __name__ == "__main__":
    main()