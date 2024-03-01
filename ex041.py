from time import strftime

# Prosfessor utilisa "from datetime import date"
# ano = date.today().year

aniversario = int(input('Qual o ano do seu aniversário: '))
ano = int(strftime('%Y'))
idade = ano - aniversario

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Voce está na categoria Mirim')
elif idade <= 14:
    print('Voce está na categoria Infantil')
elif idade <= 19:
    print('Voce está na categoria Junior')
elif idade == 20:
    print('Voce está na categoria Senior')
else:
    print('Voce está na categoria Master')
