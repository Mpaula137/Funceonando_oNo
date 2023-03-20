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