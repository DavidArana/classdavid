#David Arana Rivera
#WSQ11
print ("Este programa te va a decir cuantos numeros de cada tipo hay.")

def inversa(x):
    x =str(x)
    x = x[::-1]
    x =int(x)
    return x
num=[]
lyc=[]

menor = int(input("Dame tu numero menor: "))
mayor = int(input("Dame tu numero mayor: "))

print ("Tu rango es de :",menor," a " ,mayor)

for i in range(mayor-menor+1):
    num.append(menor)
    menor = menor+1
L=0
I=0
N=0
for i in num:
    menor = inversa(i)
    if i== menor:
        L = L+1
    else:
        E = i + menor
        menor = inversa(E)
        for q in range(30):
            if E == menor:
                I = I+1
                break
            else:
                E = E + menor
                menor = inversa(E)
                if q == 29:
                    N = l+1
                    lyc.append(i)

print ('El numero de palindromos naturales son :',L)
print ('De Non-Lychrel son:'I)
print ('Y los candidatos a Lychrel son :'N)

if N!= 0:
    print ("Y los candidatos a Lychrel son :")
    print (lyc)
