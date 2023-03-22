import operacionesimport

if __name__ == "__main__":  #Funcion principal
    A= float(input("Ingrese el primer numero:"))
    B= float(input("Ingrese el segundo numero:"))
    C= float(input("Ingrese el tercer numero:"))
    D= float(input("Ingrese el cuarto numero:"))
    E= float(input("Ingrese el quinto numero:"))
    lista =[A,B,C,D,E]
    promedio= operacionesimport.mean(lista)
    print("Este es su promedio:", str(promedio))
    mediana= operacionesimport.media_lista(lista) 
    print("ESta es su mediana:",str(mediana))
    promedioMultiplicativo= operacionesimport.promedio_multiplicativo(lista)
    print("Este es su promedio multiplicativo:",str(promedioMultiplicativo))
    ascendente= operacionesimport.ord_Ascend(lista)
    print("Esta es su lista ordenada de forma ascendente:",str(ascendente))
    descendente= operacionesimport.ord_Descen(lista)
    print("Esta es su lista ordenada de forma descendente:", str(descendente))
    potencia= operacionesimport.potencia_numeroMax_menor(lista)
    print("ESta es su potencia:",str(potencia))
    raiz= operacionesimport.Raiz_cubica(lista)
    print("ESta es la raiz cubica:",str(raiz))