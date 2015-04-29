#David Arana Rivera
def factor(n):
    x=1
    r=1
    while(x<n):
        x=x+1 #contador
        r=r*x #acumulador
    return r
def calculate_e(x):
    a=0
    for i in range(x):
        a=a+(1/(factor(i)))
    return a

#code:
n=int(input("Dime los decimales: "))
res=calculate_e(n)
print(str(res)[0:n+2])
