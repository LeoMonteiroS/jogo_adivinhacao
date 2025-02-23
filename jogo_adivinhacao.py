import random

numero_secreto = random.randint(1, 100)
chances = 0

print('Bem-Vindo ao jogo de Adivinhação! ')
print('-'*30)
print('Tente adivinhar o numero que estou pensando ')
print('-'*30)

while True:
    tentativa = int(input('Digite um numero de 1 a 100 para adivinhar: '))
    chances += 1

    if tentativa == numero_secreto:
        print(f'PARABENS! VOÇÊ ACERTOU EM {chances} tentativa(s) ')
        print('-'*30)
        sair = input('Deseja continuar? [S]im [N]ão: ')
        if sair == 'n' or sair == 'N':
             break
        else:
             chances = 0
             continue

    elif tentativa < numero_secreto:
         print('O numero secreto e maior, tente novamente ')
         print('-'*30)

    elif tentativa > numero_secreto:
            print('O numero secreto e menor, tente novamente ')
            print('-'*30)

    