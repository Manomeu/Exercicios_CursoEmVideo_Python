from random import randint
from time import sleep
print('='*30)
print('Tente adivinhar qual numero estou pensando!!!')
print('='*30)
numero = int(input('Digite o numero que o robo está pensando: '))
# lista_robo = [0, 1, 2, 3, 4, 5]
# robo = random.choice(lista_robo)
robo = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if numero == robo:
    print('Parabens, voce acertou!')
else:
    print(f'Errado, pensei no numero {robo} e não no numero {numero}')

# print('='*30)
# print('Prova Real')
# print(f'Robo: {robo}')
# print(f'Numero: {numero}')
