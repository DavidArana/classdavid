#WQS05
f=input("Dame tu temperatura en Fahrenheits: ")
c = 5 * (float (f) - 32)/9
print("Tu  temperatura en celsius seria :",int(c))
if(c>=100):
    print("¡El agua hierve a esta temperatura!!")
else:
    print("¡El agua no hierve a esta temperatura!",int(c))
