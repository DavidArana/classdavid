input("Este programa te suma el primer numero que des con el segundo ")
low=int(input("Dame el primer numero de tu rango(menor)"))
high=int(input("Dame el segundo numero(mayor)"))
su=0
while(low<=high):
    su=su+low
    low=low+1
print("Tu suma seria",su)
