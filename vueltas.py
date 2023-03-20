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
   

