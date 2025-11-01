import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('Bem vindo ao 👻🎃jogo da forca 👻🎃')
print('--------------------------------------')
print('Adivinhe a palavra antes que o fantasma se complete 👻👻👻')
print('------------------------------------------------------------')

lista_secreta_de_halloween = ['gnomo', 'duende', 'bruxa']
palavra_secreta = random.choice(lista_secreta_de_halloween)

letras_certas = []
letras_erradas = []
max_erros = 6
erros = 0

while erros < max_erros:
    nova_palavra = ''
    for letra in palavra_secreta:
        if letra in letras_certas:
            nova_palavra += letra
        else:
            nova_palavra += '_'
    print(f'Palavra: {nova_palavra}')
    
    if nova_palavra == palavra_secreta:
        print(f'🎉 Você venceu! A palavra era "{palavra_secreta}".')
        break

    letra_digitada = input('Digite uma letra👻: ').lower()

    if letra_digitada in letras_certas or letra_digitada in letras_erradas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_certas.append(letra_digitada)
    else:
        letras_erradas.append(letra_digitada)
        erros += 1
        print(f'Tente novamente 🎃 ({max_erros - erros} tentativas restantes)')

if erros == max_erros:
    print(f'💀 Você perdeu! A palavra era "{palavra_secreta}".')
