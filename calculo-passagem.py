print("Olá Bem Vindo ao software de calculo de passagem !\n Escolha o que voce deseja saber: \n 1- Quantidade de passagens geradas com valor recarregado \n 2- Valor a ser recarregado para determinado numero de passagens\n 3- Para Sair!")
while True:
    escolha=int(input("Digite a opcao desejada: \n"))
    if (escolha==1):
            passagem=float(input('Digite o Valor da Passagem:\n'))
            valorrecarga=float(input('Digite o valor recarregado:\n'))
            qtdviagens=valorrecarga/passagem
            print('A quantidade de passagens geradas com o valor recarregado e de: %.2f '%(qtdviagens))
            print ('\n\nMuito obrigado por utilizar nosso programa!\n\nAugusto Vieira!!\n\n')
    elif(escolha==2):
            viagem=int(input('Quantidade de viagens que deseja realizar:\n'))
            passagem=float(input('Digite o Valor da Passagem:\n'))
            recarga=passagem*viagem
            print('O valor a ser recarregado para %i viagens e de: %.2f'%(viagem,recarga))
            print ("\n\nMuito obrigado por utilizar nosso programa!\n\nAugusto Vieira!!\n\n")
    else:
            exit(0)