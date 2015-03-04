#WSQ10
#David Arana Rivera
import statistics
print("Este programa te va a hacer diversas operaiones con los 10 valores que le des ")
def sta(t):
    div=statistics.stdev(lista)
    return div

lista=[]
x=0
while(x<10):
    x= x+1
    num=float(input("Dime un numero: "))
    lista.append(num)

general=sum(lista)
promedio=general/10.0
has_div=sta(num)
print("Ya son los 10!!! ")

print("Tu resultado de tu division estandar seria: ",has_div)
print("Tu resultado de tu suma seria: ",int(general))
print("Tu resultado de tu promedio seria: ",promedio)
