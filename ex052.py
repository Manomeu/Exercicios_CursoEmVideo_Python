numero = int(input('Verificaremos se o numero digitado é primo: '))
soma = 0

if numero > 1 and numero != 0:
    for c in range(2, (numero + 1)):
        if numero % c == 0 and numero > 1:
            soma += 1
    if soma == 1:
        print(f'O número {numero} é primo!')
    else:
        print(f'O número {numero} não é primo!')
elif numero == 1 or numero == 0:
    print(f'O numero {numero} não entra no quadro dos primos!')
else:
    print(f'O numero {numero} é negativo e não entra no quadro dos primos!')
