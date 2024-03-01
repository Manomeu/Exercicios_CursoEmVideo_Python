nome = str(input('Qual é o seu nome completo: ')).lower().split()
# nome = nome.lower()
# nome = nome.split()
print('=' * 12)

if 'silva' in nome:
    print('O nome tem Silva')
else:
    print('O nome não tem Silva')

# Resolucao do professor
# nome = str(input('Qual o seu nome: ')).strip().lower()
# print(f'Seu nome tem Silva? {'silva' in nome}')
