def sumar(notas):
    suma=0
    for valor in notas:
        suma=suma+valor
    return suma

def contar_mayores(arreglo, valor_ref):
    contador=0
    i=0
    while i<len(arreglo):
        if arreglo[i]>80:
            contador=contador+1
        i=i+1
    return contador

def porcentaje(contadore, arreglo):
    contadorg=len(arreglo)
    porc=contadore/contadorg*100
    return porc
#cuerpo principal
notas=[80,90,100,90,70,80,0,90,0,85]
nombres=["Maria","Paula","Paola","Fabiana","Fabian","Italo","Rodrigo","Oscar","Nick","Sebastian"]
suma_notas=sumar(notas)
aprobados=contar_mayores(notas,79)
porc_aprobados=porcentaje(aprobados, notas)
print(f"Sumatoria {suma_notas}, aprobados: {aprobados}")
print(f"el {porc_aprobados}% son notas aprobadas")
