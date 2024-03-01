n1 = float(input('Qual o valor do produto comprado: '))
desconto = n1 * 0.05
valor_final = n1 - desconto
print('=============================================')
print(f'Valor inicial é de {n1:.2f} reais')
print(f'O desconto do produto é de {desconto:.2f} reais')
print(f'Valor final do produto é de {valor_final:.2f} reais')
