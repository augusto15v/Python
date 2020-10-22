#Calculadora de Baskara#


import math
print ('Calculadora de equação 2 grau')
a=int(input("Digite o valor da letra (a): \n"))
b=int(input("Digite o valor da letra (b): \n"))
c=int(input("Digite o valor da letra (c): \n"))


d= (b ** 2) - 4*a*c
print('o valor de Delta e: %.2f '%(d))


if d<0:
        print ("Raiz negativa nao pode ser extraida.")
        exit()
else:
    y=math.sqrt(d)
    x1=(-b+y)/(2*a)
    x2=(-b-y)/(2*a)
print ("\nX1 = %.2f\nX2 = %.2f " % (x1, x2))
print ("\n\nMuito obrigado por utilizar nosso programa!\n\nAugusto Vieira!!\n\n")