print(f'{"LOJA":=^40}')
valor = float(input('Qual o valor do produto: '))
print('=' * 30)
forma_pagamento = int(input('Qual é a forma que você deseja pagar?\n'
                            '1 - Á Vista no dinehrio - 10% de desconto.\n'
                            '2 - Á Vista no cartão --- 5% de desconto.\n'
                            '3 - 2X no cartão -------- Preco normal.\n'
                            '4 - 3X no cartão -------- 20% de juros. \n'
                            'Resposta: '))

if forma_pagamento == 1:
    novo_valor = valor - (valor * 0.1)
    print(f'Á vista no dinheiro, o valor do produto(R${valor:.2f}) com 10% de desconto passa a ser R${novo_valor:.2f}.')
elif forma_pagamento == 2:
    novo_valor = valor - (valor * 0.05)
    print(f'Á vista no cartão, o valor do produto(R${valor:.2f}) com 5% de desconto passa a ser R${novo_valor:.2f}.')
elif forma_pagamento == 3:
    print(f'Sua comra sera pafa em 2x parcelas de R${valor / 2}')
    print(f'Em 2X no cartão o produdo não sofre alteração de valor se mantem R${valor:.2f}. SEM JUROS')
elif forma_pagamento == 4:
    novo_valor = valor + (valor * 0.2)
    parcelas = int(input('Qual a quantidade de parcelas: '))
    print(f'Sua compra será parcelada em {parcelas}x de R${novo_valor / parcelas:.2f} COM JUROS!')
    print(f'Em 3X no cartão, o valor do produto(R${valor:.2f}) com 20% de juros passa a ser R${novo_valor:.2f}.')
else:
    print('Voce não digitou nenhuma opção valida, recomece!')
