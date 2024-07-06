def cargar(arreglo1,arreglo2,arreglo3):
    for i in range(len(arreglo1)):
        print(f"Ingrese nombre {i+1}")
        dato=input()
        arreglo1[i]=dato
        print(f"Ingrese nota parcial 1{i+1}")
        dato2=int(input())
        arreglo2[i]=dato2
        print(f"Ingrese nota parcial 1{i+1}")
        dato3=int(input())
        arreglo3[i]=dato3

def acumular(arreglo_s, a1, a2):
    for i in range(len(arreglo_s)):
        arreglo_s[i]=a1[i]+a2[i]

def promediar(prom, arreglo_s):
    for i in range(len(prom)):
        prom[i]=arreglo_s[i]/2

def imprimir(a1,a2,a3,a4,a5):
    for i in range(len(a1)):
        print(f"{a1[i]}-Parcial 1: {a2[i]}- Parcial 2:{a3[i]}- total {a4[i]} ")
        print(f"Promedio es{a5[i]}")

#cuerpo prinpcial
parcial1=[0]*3
parcial2=[0]*3
nombres=[""]*3
nota_acum=[0]*3
promedios=[0]*3
cargar(nombres, parcial1, parcial2)
acumular(nota_acum, parcial1, parcial2)
promediar(promedios,nota_acum)
imprimir(nombres, parcial1, parcial2, nota_acum,promedios)