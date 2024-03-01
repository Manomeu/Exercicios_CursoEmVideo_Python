nome = str(input('Qual o seu nome completo: ')).strip()
# nome = nome.strip()
lista_nome = nome.split()
tamanho_nome = ''.join(lista_nome)

print('=' * 12)
print(f'O nome é: {nome}.')
print(f'Nome em letras MAIUSCULAS: {nome.upper()}')
print(f'Nome em letras minusculas: {nome.lower()}')
print(f'A quantidade de letras é {len(tamanho_nome)}')
# Outro metodo acima é {len(nome) - nome.count(' ')} | Diminuindo o numero de espacos do nome
print(f'Primeiro nome é {lista_nome[0]} e tem {len(lista_nome[0])} letras.')
# Outro metodo acima é usar o primeiro espaço como busca {nome.find(' ')}
