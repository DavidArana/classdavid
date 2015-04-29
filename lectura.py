#Examen
import statistics
def readNumbersFromFile():
    numeros=[]
    texto=open("numeros.txt","r")#aqui abre el documento
    lineas=0
    total=0

    for valor in texto:
        total=total+int(valor)
        lineas=lineas+1
        numeros.append(int(valor))
    std=statistics.stdev(numeros)
    promedio=total/lineas

    print("Tu suma es: ",total)
    print("Tus numeros son", lineas)
    print("Tu promedio es: ",promedio)
    print("Y tu SD es: ",std )

readNumbersFromFile()
