from datetime import date
print('Programa para verificar quem ainda não fez 21 anos!')
ano = date.today().year
menores = 0
maiores = 0

for i in range(0, 7):
    idade = int(input('Qual ano de nascimento? (YYYY) '))
    if idade <= ano - 21:
        maiores += 1
    elif idade > ano - 21:
        menores += 1

if 7 > menores > 1:
    print(f'{menores} pessoas ainda não alcançaram a maioridade e {maiores} já!')
elif menores == 1:
    print(f'{menores} pessoa ainda não alcançou a maioridade e {maiores} já!')
elif menores == 7:
    print(f'Todos são de menores!')
else:
    print(f'Todos já acançaram a maioridade!')

