#David Arana Rivera
#WSQ09-Factorial Calculator
print("Este programa te ayuda a encontrar el factorial de un numero")
preg=""
while(preg!="n"):
    n=int(input("Dame un numero positivo: "))
    acumulador=1
    contador=2
    if(n<0):
        print("Porfavor intentalo otra vez!!")
    else:
        while(contador<=n):
            acumulador=acumulador*contador
            contador=contador+1
        print("Tu respuesta seria: ",acumulador)
    preg=str(input("Deseas continuar y o n: "))
input("Ten un buen dia!!")
