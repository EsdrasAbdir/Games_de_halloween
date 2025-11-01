""" Advinhação do segredo da bruxa """

import random 
import os

os.system('cls')

print('🎃👻 Bem-vindo a cabana da bruxa 🎃👻')
print('----------------------------------------')
print('A brua de Salem guardou um Número secreto 🧟 em seu caldeirão🐈‍⬛')
print('-------------------------------------------------------------')
print('Você tem poucas chances para descobrir, ou um 🧛🕸️ feitiço🧛🕸️ cairá sobre você\n')

numero_secreto = random.randint(1,50)

contador=0
while contador < 7:
    numero_da_tentativa = int(input('Digite o número misterioso de 1 até 50😈👻: '))
    contador += 1

    try:
        if numero_secreto == numero_da_tentativa:
            print('Você quebrou o feitiço🎃!!!!')

        else:
            print(f'Você errou o número, o número era {numero_secreto}🎃 🕸️ TENTE NOVAMENTE🕸️')
    except ValueError:
        print(f'Esse número {numero_da_tentativa} é inválido 👺')
