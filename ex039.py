from time import strftime

print('Programa para calcular alistamento Obrigatório no Brasil')
sexo = str(input('Você é homem ou mulher: ')).lower().strip()

if sexo == 'mulher':
    print('Você não é obrigada a se alistar no Brasil!')
elif sexo == 'homem':
    aniversario = int(input('Qual o ano do seu aniversário: '))
    ano = int(strftime('%Y'))
    idade = ano - aniversario

# Provessor utiliza "from datetime import date"
# ano = date.today().year

    print(f'Você nasceu em {aniversario}, então tem {idade} anos em {ano}.')

    if idade == 18:
        print('Está na hora de se alistar!')
    elif idade < 18:
        print('Ainda faltam ', 18 - idade, 'anos para se alistar!')
        print(f'O alistamento será em {aniversario + 18}')
    elif idade > 18:
        print('Você já se alistou a', idade - 18, f'anos!')
        print(f'O alistamento foi em {aniversario + 18}')
