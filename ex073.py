times_brasileirao = (
    "Palmeiras",
    "Grêmio",
    "Atlético-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "Chapecoense",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG"
)
cont = 0
print('+_+_+_+_+_+_+_TABELA DO BRASILEIRAO_+_+_+_+_+_+_+_+_+')
print(times_brasileirao)
print('+_+_+_+_+_+_+__+_+_+_+_+_+_+_+_+')
print(f'Os 5 primeiros colocados são: {times_brasileirao[0:5]}')
print(f'Os 4 ultimos colocados são: {times_brasileirao[-4:]}')
print('+_+_+_+_+_+_+__+_+_+_+_+_+_+_+_+')
print('Tabela em ordem alfabetica:')
print(sorted(times_brasileirao))
print('+_+_+_+_+_+_+__+_+_+_+_+_+_+_+_+')
for i in times_brasileirao:
    cont += 1
    if i == 'Chapecoense':
        print(f'O time da chapecoense está na posição {cont}')
