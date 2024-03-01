from random import randint
from time import sleep
valor = 0
robo = randint(0, 10)
contador = 1
print('='*30)
print('Tente adivinhar qual numero estou pensando entre 0 e 10!!!')
print('='*30)
# while valor == 0:
#     numero = int(input('Digite o numero que o robo está pensando: '))
#     print('PROCESSANDO...')
#     sleep(1)
#     if numero != robo:
#         if numero > robo:
#             print('Menor, tente novamente!')
#             contador += 1
#         elif numero < robo:
#             print('Maior, tente novamente!')
#             contador += 1
#     else:
#         print(f'Acertou, pensei no numero {robo} e voce escolheu o numero {numero}')
#         print(f'Voce digitou {contador} vezes!')
#         break

######## Professor utiliza (acertou = false) para iniciar o while
acertou = False
contador = 0
while not acertou:
    numero = int(input('Digite o numero que o robo está pensando: '))
    print('PROCESSANDO...')
    contador += 1
    sleep(1)
    if numero == robo:
        acertou = True
    else:
        if numero > robo:
            print('Menor, tente novamente!')
        elif numero < robo:
            print('Maior, tente novamente!')
print(f'Acertou, pensei no numero {robo} e voce escolheu o numero {numero}')
print(f'Voce digitou {contador} vezes!')
