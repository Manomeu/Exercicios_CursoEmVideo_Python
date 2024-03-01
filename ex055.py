print('Programa para ver quem é o mais pesado e quem é o mais leve:')
###########metodo sem for###############
# peso1 = float(input('Qual seu peso: '))
# peso2 = float(input('Qual seu peso: '))
# peso3 = float(input('Qual seu peso: '))
#
# if peso1 > peso2 > peso3:
#     print(f'Maior peso {peso1}, menos peso {peso3}')
# elif peso2 > peso1 > peso3:
#     print(f'Maior peso {peso2}, menos peso {peso3}')
# elif peso3 > peso1 > peso2:
#     print(f'Maior peso {peso3}, menos peso {peso2}')
# elif peso2 > peso3 > peso1:
#     print(f'Maior peso {peso2}, menos peso {peso1}')
# elif peso3 > peso2 > peso1:
#     print(f'Maior peso {peso3}, menos peso {peso1}')
# elif peso1 > peso3 > peso2:
#     print(f'Maior peso {peso1}, menos peso {peso2}')

###################metodo for###############
maior = 0
# menor = 999999 ---- professos ensina a verificar o peso no primeiro registro
menor = 0
for i in range(1, 6):
    peso = float(input(f'Peso da pessoa {i}?'))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior} e o menor é {menor}')