nome = str(input('Digite o seu nome: ')).strip()
nome2 = nome.split()

print('=' * 12)
print(f'O nome é {nome}.')
print(f'O primeiro nome é {nome2[0]}.')
print(f'O ultimo nome é {nome2[-1]}.') # Resolução do Prof: print(f'O ultimo nome é {nome2[len(nome)-1]}.')

