def triangulo(longitud):
    conta = 0
    while(longitud >= conta):
        print("T"*conta)
        conta  = conta + 1


    while(conta>= 1):
        print("T"*(conta-2))
        conta = conta - 1
    return triangulo


preg=int(input("Dime que tan grande quieres tu triangulo: "))
triangulo(preg)
