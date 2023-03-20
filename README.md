# Funceonando_oNo
Probaremos las funciones que nos presentaron en clase, #Reto06 

Este respositorio que a continuación presentare tiene el intento de solucion sobre las funciones pedidas en el reto.

## Punto 1:
Dado la figura de la imagen, desarrolle:

[![image.png](https://i.postimg.cc/xdtdGZF3/image.png)](https://postimg.cc/xkNYn6QX)

- Una función matemática para calcular el volumen y el área superficial.

- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

- Revise como utilizar el valor de pi usando import math y math.pi

## Punto 2:

Dado la figura de la imagen, desarrolle:

[![image.png](https://i.postimg.cc/GmM2GNfJ/image.png)](https://postimg.cc/WdkTP9Th)

- Una función matemática para calcular el área y el perimetro.

- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.

- Revise como utilizar el valor de pi usando import math y math.pi

## Punto 3:

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```
def calcula_cant_carne_en_Aves ( N:int, M:int ,K:int) : #se declaran

 total_de_carne = (N*6)+(M*7)+(K*1) # operacion principal (6 de gallinas, 7 de gallos, 1 de pollitos) #peso en kg
 Cant_kilos= total_de_carne/1000
 return Cant_kilos#lo que debe arrojar la funcion

if __name__ == "__main__":  #Funcion principal
    N = int(input("ingrese numero de gallinas: "))
    M = int(input("ingrese numero de gallos: "))
    K = int(input("ingrese numero de pollitos: "))
    total = calcula_cant_carne_en_Aves(N,M,K)
print ("El total de carne de aves es:"+ str(total)+"Kg")

```
## Punto 4:
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```
def calcular_las_vueltas (P:int, M:int, H:int, B:float) :# ((cant) P: panes, M:bolsas de leche, H: huevos, B: cantidad de dinero )
    Preciototal = ((P*300)+(M*3300)+(H*350)) # (precio de pan, bolsa de leche y huevos)
    vueltas= B - Preciototal
    return vueltas
if __name__ == "__main__":  #Funcion principal
    P= int(input("ingrese la cantidad de panes:"))
    M= int(input("ingrese la cantidad de bolsa (s) de leche:"))
    H= int(input("ingrese la cantidad de huevos:"))
    B=float (input("cantidad de dinero con el que va a pagar:"))
    total_vueltas= calcular_las_vueltas (P, M, H, B)
if calcular_las_vueltas < 0 :
    print ("Te falto"+ str(total_vueltas))
else:
    print ("El total a devolver es:"+ str(total_vueltas))
   
```

## Punto 5:
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```
def valor_total_prestamo( C: float,i: float,n:int):
     valor = C * ((1 + i)**n)
     return valor

if __name__ == "__main__":  #Funcion principal
     C= float(input("Ingrese el valor del prestamo:"))
     i= float(input("Ingrese el valor del interes: "))
     n= int(input("Ingrese el numero de meses de prestamo:"))

valor_a_pagar= valor_total_prestamo(C, i,n)
print("El valor total a pagar es:" + str(valor_a_pagar))

```

