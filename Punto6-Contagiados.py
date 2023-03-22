def contagiados_porDias(C:int,D:int):
    total_contagiadoscovid = C * (2**D) #operacion para hallar contagiados a partir de dias
    return total_contagiadoscovid
if __name__ == "__main__":  #Funcion principal
    C = int(input("Ingrese el numero de contagiados actuales:"))
    D = int(input("Ingrese el numeros de dias transcurridos:"))

covid_contagiados= contagiados_porDias (C,D)
print("El total de contagiados despues de transcurrir", D, "días es de:"+ str(covid_contagiados))
