def valor_total_prestamo( C: float,i: float,n:int):
     valor = C * ((1 + i)**n)
     return valor

if __name__ == "__main__":  #Funcion principal
     C= float(input("Ingrese el valor del prestamo:"))
     i= float(input("Ingrese el valor del interes: "))
     n= int(input("Ingrese el numero de meses de prestamo:"))

valor_a_pagar= valor_total_prestamo(C, i,n)
print("El valor total a pagar es:" + str(valor_a_pagar))