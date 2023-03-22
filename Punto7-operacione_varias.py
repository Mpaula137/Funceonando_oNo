
import math
def promedio_multiplicativo(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto ** (1/len(lista))
def ord_Ascend(lista):
    return sorted(lista)
def ord_Descen(lista):
    return sorted(lista,reverse= True)
def potencia_numeroMax_menor(lista):
    return max(lista)**min(lista)
def Raiz_cubica(list):
    return math.pow(min(list), 1/3)
from statistics import* #importamos operaciones desde el modulo statictics
 
if __name__ == "__main__":  #Funcion principal
    A= float(input("Ingrese el primer numero:"))
    B= float(input("Ingrese el segundo numero:"))
    C= float(input("Ingrese el tercer numero:"))
    D= float(input("Ingrese el cuarto numero:"))
    E= float(input("Ingrese el quinto numero:"))
lista= [A,B,C,D,E]
xSquared1 = mean(lista) #promedio
xSquared2 = median(lista)#promedio
 
print ("Este es su promedio:"+str(xSquared1))
print("Este es la mediana de su lista:"+str(xSquared2))
print("Este es tu promedio multiplicativo:"+str(promedio_multiplicativo(lista)))
print("Esta es tu lista de foma ascendente:"+str(ord_Ascend(lista)))
print("Esta es tu lista de foma descendiente:"+str(ord_Descen(lista)))
print("Esta es tu potencia:"+str(potencia_numeroMax_menor(lista)))
print("Esta es tu raiz cubica del numero menor:", Raiz_cubica(lista))

 



