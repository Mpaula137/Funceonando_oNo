import math #importamos math para usar pi y la raiz del area
def volumen(r1, r2, h):
    volumenfig=(1/3)*math.pi*h*(r1**2+r1*r2+r2**2) #V = (1/3)πh(r1^2 + r1r2 + r2^2)
    return volumenfig
def are_superficial (r1, r2, h):
    Are_super = math.pi*(r1+r2)*math.sqrt((r1-r2)**2 + h**2)+ math.pi*(r1**2+r2**2)#A = π(r1 + r2)√((r1 - r2)^2 + h^2) + π(r1^2 + r2^2)
    return Are_super
if __name__ == "__main__":  #Funcion principal
    r1= float(input("Ingrese el radio 1:"))
    r2=float(input("Ingrese el radio 2:"))
    h= float(input("Ingrese la altura:"))
    print("Este es el volumen del tronco del cono:",str(volumen(r1,r2,h)),"cm cubicos")
    print("Esta es la area superficial del tronco del cono:"+ str(are_superficial(r1,r2,h)),"cm cuadrados")
