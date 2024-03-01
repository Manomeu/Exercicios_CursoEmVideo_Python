dia = float(input('Quantos dias alugado: '))
km = float(input('Quantos Km rodados: '))
custo_km = 0.15
custo_dia = 60
custo_total = dia * custo_dia + km * custo_km
# ou colocar a expressao direta abaixo
# custo_total = dia * 0.15 + km * custo_km
print(f'O valor do carro foi de {custo_total:.2f} reais')
