#Examen
def findthrees(number):
    suma=0
    for i in number:
        if(i%3==0):
            suma=suma+i
    return suma
Lista=[0,4,2,6,9,8,3,12]
print(findthrees(Lista))
