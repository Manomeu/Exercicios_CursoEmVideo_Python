numero1 = int(input('\033[30;44mDigite o primeiro número\033[m'))
numero2 = int(input('\033[40;34mDigite o segundo número\033[m'))
soma = numero1 + numero2

print('\033[36mA soma entre {} e {} é: {}\033[m'.format(numero1, numero2, soma))
