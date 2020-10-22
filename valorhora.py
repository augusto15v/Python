#-*- utf-8 -*-#
nome=input("Digite seu nome completo: ")

jornadasemanal=(44)

semanames= input('digite a quantidade de semanas do mes: ')
sm=int(semanames)


jornadamensal=jornadasemanal*sm


sb= input('digite seu salario bruto: ')
salariobruto=float(sb)

valorhora= salariobruto/jornadamensal

print ('Prezado %s , voce trabalhou %s horas este mes, entao o valor da sua hora foi de: R$%.2f' %(nome,jornadamensal,valorhora)) #exibe o resultado
