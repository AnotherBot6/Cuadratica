
import math

def comprobacion(A, B, C):
    if A==0 and B==0:
        return('No')
    elif A==0 and B!=0:
        return('Ok')
    elif A!=0 and B!=0:
        return('OK')
    
    

def valorx(B, C):
    v=-C/B
    return(v)

def disc(A, B, C):
    N=(B**2)-(4*A*C)
    if N==0:
        resultado=(-1*B)/(2*A)
        print(resultado)
        
    elif N<0:
        print('Complex roots')
        
    else:
        raiz=math.sqrt(N)
        resultado_1=((-1*B)+raiz)/(2*A)
        resultado_2=((-1*B)-raiz)/(2*A)
        print(resultado_1)
        print(resultado_2)

A=float(input('Ingrese el valor a: '))
B=float(input('Ingrese el valor b: '))
C=float(input('Ingrese el valor c: '))
res=comprobacion(A, B, C)

if res=='Ok':
    constante=valorx(B, C)
    print(constante)
                     
elif res=='OK':
    disc(A, B, C)

else:   
    print('Sin solucion')
