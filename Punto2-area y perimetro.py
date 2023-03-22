import math
def perimetro_fig(r, a, b):
    logitudArco = math.pi *r /2
    perimetro_rect= 2*a + 2*b
    perimetroTotal= logitudArco+perimetro_rect
    return perimetroTotal
def Area_fig (r,a ,b):
    areaCircular= math.pi * r**2
    areaRectan= b*a
    areaTotal= areaCircular+areaRectan
    return areaTotal
if __name__ == "__main__":  #Funcion principal
    r=float(input("ingrese el radio:"))
    a=float(input("Ingrese la medida de el primer lado:"))
    b=float(input("Ingrese la medida de el segundo lado"))
print("Este es el perimetro de la figura:",str(perimetro_fig(r,a,b)))
print("Esta es la area de la figura:",str(Area_fig(r,a,b)))
