print('=+' * 15)
print(f'{'Banco':^40}')
print('=+' * 15)
saque = int(input('Qual valor voce quer sacar? R$'))
valor1 = 50
valor2 = 20
valor3 = 10
valor4 = 1
sobra = 0
while True:
    sobra = saque
    if 50 <= sobra:
        print(f'Total de {saque // valor1} notas de R$50!')
        sobra = saque % valor1
        if sobra == 0:
            break
    if 20 <= sobra < 50:
        print(f'Total de {sobra // valor2} notas de R$20!')
        sobra = sobra % valor2
        if sobra == 0:
            break
    if 10 <= sobra < 20:
        print(f'Total de {sobra // valor3} notas de R$10!')
        sobra = sobra % valor3
        if sobra == 0:
            break
    if 1 <= sobra < 10:
        print(f'Total de {sobra // valor4} notas de R$1!')
        break
print('-=' * 30)
print('Volte sempre!')

# Professor faz a validação completamente diferente.
# saque = int(input('Qual valor voce quer sacar? R$'))
# total = saque
# valor = 50
# totalcedula = 0
# while True:
#     #se maior que 50(na primeira validação) valida a quantidade de cedulas que sera sacadas.
#     if total >= valor:
#         total -= valor
#         totalcedula += 1
#     # Após a validação das notas de 50, vai validando se teria necessidade das demais notas e mostrando na tela
#     else:
#         if totalcedula > 0:
#             print(f'Total de {totalcedula} notas de R${valor}!')
#         if valor == 50:
#             valor = 20
#         elif valor == 20:
#             valor = 10
#         elif valor == 10:
#             valor = 1
#         if totalcedula == 0:
#             break
# print('-=' * 30)
# print('Volte sempre!')
