#WSQ13
#David Arana Rivera
def baby(raiz):
    if(raiz==0):
        return print("Tu resultado seria: ",raiz)
    elif(raiz<0):
        return print("Error.La raiz no puede ser negativa")
    else:
        potencia=0
        sumador=0
        while(potencia<raiz):
             potencia=sumador**2
             sumador=sumador+1

        if(potencia==raiz):
            return sumador-1

        else:
            adivina=sumador-1
            ecuacion=(adivina+(raiz/adivina))*.5
            while(ecuacion!=adivina):
                adivina=ecuacion
                ecuacion=(adivina+(raiz/adivina))*.5
            return ecuacion

num=float(input("Dime la raiz que quieres saber: "))
print(baby(num))
