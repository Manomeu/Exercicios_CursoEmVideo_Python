print('-' * 30)
print('     Loja do Manomeu')
print('-' * 30)
mais_de_mil = mais_barato = total = 0
nome_mais_barato = ''
while True:
    nome = str(input('Qual o nome do produto: ')).strip().lower()
    preco = float(input('Preço: R$'))
    total += preco
    #primeira validação do menor preço
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    if preco > 1000:
        mais_de_mil += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    # Valida se continuar é S ou N, caso não, continua repetindo a pergunta.
    while continuar not in 'sn':
            continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar in 'n':
        break
# print('=+' * 13 + 'RESULTADO' + '=+' * 13)
print(f'{'RESULTADO':-^60}')
print(f'O total gasto na compra foi R${total:.2f}')
print(f'Foram {mais_de_mil} produtos com mais de R$1000.00 reais')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${mais_barato:.2f}')
print('=+' * 30)
