print('Programa para somar os numeros pares:')
soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i} numero: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f'A soma de {cont} numeros e apenas dos numeros pares é:', soma)
