frase = str(input('Digite uma frase qualquer: ')).lower().strip()
# frase = frase.lower()
letraa = frase.count('a')
primeiroa = frase.find('a')
segundoa = frase.rfind('a')

if 'a' in frase:
    print('=' * 12)
    print(f'A letra a aparece {letraa} vezes na frase.')
    print(f'A primeira letra a se encontra na posição {primeiroa + 1}')
    print(f'A ultuma letra a se encontra na posição {segundoa + 1}')
else:
    print('Não tem letra a.')

# Professor não criou variaveis, já realizou os processos dentro do print
# print('=' * 12)
# print(f'A letra a aparece {frase.count('a')} vezes na frase.')
# print(f'A primeira letra a se encontra na posição {frase.find('a') + 1}')
# print(f'A ultuma letra a se encontra na posição {frase.rfind('a') + 1}')
