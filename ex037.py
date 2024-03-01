numero = int(input('Digite um numero inteiro: '))
base = input('Qual a base decimal voce deseja escolher?\n'
             '1 - Binário\n'
             '2 - Octal\n'
             '3 - Hexadecimal\n'
             'Opção: ')

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if base == '1':
    print(f'Convertendo o numero {numero} para Binário: {binario[2::]}')
elif base == '2':
    print(f'Convertendo o numero {numero} para Octal: {octal[2::]}')
elif base == '3':
    print(f'Convertendo o numero {numero} para Hexadecimal: {hexadecimal[2::]}')
else:
    print('Voce não digitou nenhum numero!')
