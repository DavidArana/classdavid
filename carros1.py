def carro(file):
  c=0
  sumaprecio=0
  sumaciudad=0
  sumalto=0
  for line in file:
    c=c+1
    if(c%2==1):
      precio=line[42:46]
      precios=float(price)
      sumaprecio=sumaprecio+ precios
      ciudad=line[52:54]
      ciudades=float(ciudad)
      sumaciudad=sumaciudad+ciudades
      alto=line[55:57]
      altos=float(alto)
      sumalto=sumalto+altos
    carros=c/2
    promedio_precio=sumaprecio/cars
    promedio_ciudad=sumaciudad/cars
    promedio_alto=sumalto/cars
    return(promedio_precio,promedio_ciudad,  promedio_alto)
texto=open("cars.dat.txt")
(a,b,c)=carro(texto)
a=str(a)
b=str(b)
c=str(c)
print("El promedio es: ",a[0:5])
print("El promedio es: ",b[0:5])
print("El promedio es: ",c[0:5])
