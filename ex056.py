print('Programa 56')
maisvelho = 0
contador = 0
media = 0
somaidade = 0
nomedovelho = ''
for i in range(1, 5):
    print(f'====== PESSOA {i} ========')
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual o sexo? [M/F] ')).lower()
    somaidade += idade
    media = somaidade / i
    if sexo == 'f' and idade < 21:
        contador += 1
    if sexo == 'm' and idade > maisvelho:
        maisvelho = idade
        nomedovelho = nome
print(f'Media das idades é {media}')
print(f'Teste mais velho se chama {nomedovelho} e tem {maisvelho} anos.')
print(f'Temos {contador} mulheres mais nova que 21 anos.')

