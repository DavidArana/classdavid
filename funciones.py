#David Arana Rivera
#WSQ08
def suma(x,y):
    respuesta=x+y
    return respuesta
def resta(x,y):
    respuesta=x-y
    return respuesta
def divicion(x,y):
    respuesta=x/y
    return respuesta
def multi(x,y):
    respuesta=x*y
    return respuesta
def resi(x,y):
    respuesta=x%y
    return respuesta

input("Este programa hace operaciones con los numeros que le des.")
primero=int(input("Dame tu primer numero: "))
segundo=int(input("Dame tu segundo numero: "))

has_suma=suma(primero,segundo)
has_resta=resta(primero,segundo)
has_divicion=divicion(primero,segundo)
has_multi=multi(primero,segundo)
has_resi=resi(primero,segundo)

print("Tu suma seria: ",has_suma)
print("Tu resta seria: ",has_resta)
print("Tu divicion seria: ",float(has_divicion))
print("Tu multiplicacion seria: ",has_multi)
print("Tu residuo seria: ",float(has_resi))
