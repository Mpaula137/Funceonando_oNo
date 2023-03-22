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
def promedio_Total(lista):
    return sum(lista)/len(lista)
def media_lista(lista):
   return median(lista)
