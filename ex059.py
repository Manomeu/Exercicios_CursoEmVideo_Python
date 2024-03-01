from time import sleep
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o primeiro numero: '))
valor = 0
### professor usa o while com valor != 5 para que o programa pare em 5
while valor == 0:
###### professor usa o print do menu com '''tres aspas '''

    print('+=' * 20)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Numeros')
    print('[5] Sair do programa')
    menu = int(input('Escolha o que deseja fazer com os numeros escolhidos:'))
    if menu == 1:
        print('+=' * 20)
        print('Voce escolheu somar!')
        print(f'A soma dos numeros é: {n1} + {n2} = {(n1 + n2)}')
    elif menu == 2:
        print('+=' * 20)
        print('Voce escolheu multiplicar!')
        print(f'A multiplicação dos numeros é: {n1} x {n2} = {(n1 * n2)}')
    elif menu == 3:
        print('+=' * 20)
        print('Voce escolheu o maior!')
        if n1 > n2:
            print(f'O maior numeros é: {n1}')
        elif n2 > n1:
            print(f'O maior numeros é: {n2}')
        else:
            print('Os dois possuem o mesmo valor!')
    elif menu == 4:
        print('+=' * 20)
        print('Vamos escolher novos numeros:')
        n1 = float(input('Digite o NOVO primeiro numero: '))
        n2 = float(input('Digite o NOVO primeiro numero: '))
    elif menu == 5:
        print('Finalizando!')
        sleep(1)
        break
    elif menu >= 5 or menu <= 0:
        print('Opção invalida!')
print('+=' * 20)
print('Programa encerrado!')
