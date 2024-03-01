n1 = int(input('Numero 1'))
n2 = int(input('Numero 2'))
n3 = int(input('Numero 3'))

print(f'Os numeros escolhidos foram: {n1}, {n2} e {n3}')
if n2 < n1 > n3:
    print(f'O maior numero é {n1}')
    if n2 > n3:
        print(f'O menos número é {n3}')
    else:
        print(f'O menos numero é {n2}')

if n1 < n2 > n3:
    print(f'O maior numero é {n2}')
    if n1 > n3:
        print(f'O menos número é {n3}')
    else:
        print(f'O menos numero é {n1}')

if n1 < n3 > n2:
    print(f'O maior numero é {n3}')
    if n1 > n2:
        print(f'O menos número é {n2}')
    else:
        print(f'O menos numero é {n1}')

# resolução do professor, mais simples
# Ja indica um maior e um menor, caso entre no if a variavel é alterada
# maior = n1
# menor = n1
# Verifica se são maiores
# if n1 < n2 > n3:
#     maior = n2
# if n1 < n3 > n2:
#     maior = n3
# Verifica se são menores
# if n1 > n2 < n3:
#     menor = n2
# if n1 > n3 < n2:
#     menor = n3

