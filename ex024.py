cidade = str(input('Qual o nome da cidade: ')).lower()
# cidade = cidade.lower()
ésanto = cidade.split()
print('=' * 12)

if ésanto[0] == 'santo':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com santo')

# Resolucao do professor
# cidade = str(input('Qual o nome da cidade: ')).strip().lower()
# print(cidade[:5] == 'santo')
