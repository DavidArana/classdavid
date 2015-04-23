#Examen2
def dotproduct(v1,v2):
    if(len(v1)==len(v2)):
        suma=0
        for a in range (len(v1)):
            suma=suma+((v1[a])*(v2[a]))
        return suma
    else:
        print("Error.No son el mismo tamaño de vectores ")
        return  -1



lista1=[2,4,5,6]
lista2=[1,2,3,4]
print(dotproduct(lista1,lista2))
