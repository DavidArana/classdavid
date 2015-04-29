def check_banana(a):
    text=open("banana.txt",'r')
    cantidad=0
    for ba in text:
        minu=ba.lower() #convierte las palabras a letras minusculas
        sub=minu.find('banana') #busca la palabra dentro del archivo
        while sub !=-1:
            cantidad=cantidad+1
            sub=minu.find('banana',(sub+1))
    return(cantidad)
    close("banana.txt")

number=check_banana('banana.txt')
print("la palabra banana aparece ",number," veces en el archivo")
