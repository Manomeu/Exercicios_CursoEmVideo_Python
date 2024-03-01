distancia = int(input('Qual a distancia em Km da viagem? '))

if distancia <= 200:
    print(f'Voce sera cobrando em R${distancia * 0.5:.2f}')
else:
    print(f'Voce sera cobrado em R${distancia * 0.45:.2f}')

# Simplificado
# preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
