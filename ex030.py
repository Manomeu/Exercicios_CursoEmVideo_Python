numero = int(input('Digite um numero e mostrarei se é par ou impar: '))
resto = numero % 2

if resto == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')
