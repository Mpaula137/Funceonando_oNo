# Funceonando_oNo
Probaremos las funciones que nos presentaron en clase, #Reto06 

Este respositorio que a continuación presentare tiene el intento de solucion sobre las funciones pedidas en el reto.

## Punto 1:
Dado la figura de la imagen, desarrolle:

[![image.png](https://i.postimg.cc/xdtdGZF3/image.png)](https://postimg.cc/xkNYn6QX)

- Una función matemática para calcular el volumen y el área superficial.

- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

- Revise como utilizar el valor de pi usando import math y math.pi

Explicación: Investigue y se usa el math.pi para dar el valor de pi, luego encontre las formulas y fue ponerlas en una funcion y pedir que el programa lo realizara con ayuda del usuario, ya que este va a dar los valores correspondientes.
```
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
```
## Punto 2:

Dado la figura de la imagen, desarrolle:

[![image.png](https://i.postimg.cc/GmM2GNfJ/image.png)](https://postimg.cc/WdkTP9Th)

- Una función matemática para calcular el área y el perimetro.

- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.

- Revise como utilizar el valor de pi usando import math y math.pi

## Punto 3:

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

Explicacion: Encontramos una operacion simple ya que es multiplicar los kilos por la cantidad de animales y luego dividilas para que quede en kilos, ya luego puse la funcion main.

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

Explicacion: Por lógica cree la funcion de como se devolverian las vueltas luego dejo que el usuario ponga los valoes llamo la funcion y pues esta hara el proceso, luego veremos que hay un condicional que dara como resultado, si falta o te sobra.

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
if total_vueltas > 0 :
   print ("El total a devolver es:"+ str(total_vueltas))
else:
   print("Te falto:"+ str(total_vueltas))
   
```

## Punto 5:
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

Explicación: Busque primero la formula de interes compuesto aplicado a prestamo, cree la funcion y luego nombre, deje el proceso para que el usuario interactue con el codigo y llame la funcion para que se operara.

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
## Punto  6:
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

Explicación: Luego de analizarlo y encontar la formula central, entable la funcion, luego las nombre y opere llamando la misma.
 
 ```
 def contagiados_porDias(C:int,D:int):
    total_contagiadoscovid = C * (2**D) #operacion para hallar contagiados a partir de dias
    return total_contagiadoscovid
if __name__ == "__main__":  #Funcion principal
    C = int(input("Ingrese el numero de contagiados actuales:"))
    D = int(input("Ingrese el numeros de dias transcurridos:"))

covid_contagiados= contagiados_porDias (C,D)
print("El total de contagiados despues de transcurrir", D, "días es de:"+ str(covid_contagiados))
```

## Punto 7:
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

Explicación: Lo primero que hice fue importar la funcion math para poder hallar la raiz esta se hace con mat.pow entre parentesis se pone la base y el exponente, luego declare las demas funciones como el promedio multiplicativo, el orden descendiente y ascendente(sort), luego la potencia usando(min,max), lueego pedi al usuario ingresar los 5 numeros, cree la lista y ahi importe la funcion statistic para hallar promedio y media.

```

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
```
 ## Punto 9:
 Consultar qué es y cómo funciona pip en python
  ## pip
Es el sistema de gestión de paquetes de Python, que se utiliza para instalar y administrar paquetes de software escritos en Python. Un paquete es un conjunto de módulos que ofrecen una funcionalidad específica y que pueden ser reutilizados en diferentes proyectos.

El funcionamiento de pip es sencillo: se conecta al repositorio de paquetes de Python (Python Package Index o PyPI) y descarga e instala los paquetes necesarios para nuestro proyecto. PyPI es una base de datos pública de paquetes de software de Python, que contiene más de 300,000 paquetes. La mayoría de los paquetes son de código abierto y gratuitos.

También es posible crear un archivo de requisitos requirements.txt, que lista todos los paquetes necesarios para el proyecto, junto con sus versiones. Esto permite compartir fácilmente los paquetes necesarios para que otros usuarios puedan instalarlos rápidamente en su propio entorno de Python.

pip también permite actualizar los paquetes instalados en un proyecto. Para hacer esto, se puede utilizar el siguiente comando:
```
pip install --upgrade nombre_del_paquete
```
## Punto 10:
Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

- NumPy: es una biblioteca para el lenguaje de programación Python, añade soporte para grandes matrices y matrices multidimensionales, junto con una amplia colección de funciones matemáticas de alto nivel para operar en estas matrices.

- Pandas: es una biblioteca de análisis de datos para Python que proporciona estructuras de datos flexibles y de alto rendimiento para trabajar con datos tabulares y series de tiempo.

- Matplotlib: es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en Python. Proporciona una API para la generación de gráficos en 2D con Python y se puede utilizar para crear gráficos de barras, gráficos de líneas, histogramas, gráficos de dispersión, etc.

- Scikit-learn: es una biblioteca de aprendizaje automático para Python que proporciona herramientas simples y eficientes para la minería y el análisis de datos. Proporciona una amplia gama de algoritmos de aprendizaje automático, como regresión lineal, SVM, árboles de decisión, etc.

- TensorFlow: es una plataforma de software de código abierto para el aprendizaje automático desarrollada por Google Brain Team. Permite la construcción y entrenamiento de modelos de aprendizaje automático utilizando redes neuronales.

- Keras: es una biblioteca de redes neuronales de alto nivel que se ejecuta sobre TensorFlow. Proporciona una API fácil de usar para la construcción de modelos de aprendizaje profundo y es compatible con los principales marcos de redes neuronales, como TensorFlow, CNTK y Theano.

- Flask: es un microframework para Python utilizado para el desarrollo de aplicaciones web. Proporciona herramientas para la gestión de solicitudes HTTP, el renderizado de plantillas, la gestión de sesiones y la autenticación de usuarios, entre otras funcionalidades.

- Django: es un framework de desarrollo web de alto nivel para Python que permite construir aplicaciones web complejas de manera rápida y eficiente. Proporciona herramientas para la gestión de bases de datos, el manejo de formularios, la autenticación de usuarios y la generación automática de la interfaz de usuario.

Para usar pip, se debe abrir una terminal y escribir el siguiente comando:
```
pip install nombre_del_paquete
```
Este comando descargará e instalará el paquete especificado en el proyecto.
 # Bueno!! aca termina este reto #06 nos encontraremos en el proximo, aunque ya son mas seguidos que antes xd
