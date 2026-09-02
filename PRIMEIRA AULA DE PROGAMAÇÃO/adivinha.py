import random

print('jogo do adivinha')
print('Adivinhe o número entre 1 e 100! Você tem 7 tentativas.')

numero_secreto = random.randint(1, 100)
tentativa = int(input('Digite seu palpite: '))

contador = 7
while contador > 0:
    print(f"\nTentativas restantes: {contador}")

    if tentativa == numero_secreto:
        print('Parabéns! Você acertou!')
        break
    elif tentativa < numero_secreto:
        print('O número secreto é maior que', tentativa)
    else:
        print('O número secreto é menor que', tentativa)

    contador -= 1
    if contador > 0:
        tentativa = int(input('Digite seu palpite: '))

if contador == 0:
    print('Você perdeu! O número secreto era:', numero_secreto)
