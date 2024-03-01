from datetime import date
ano = int(input('Digite o ano ou coloque 0 para escolher o ano atual:'))
if ano == 0:
    ano = date.today().year # pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')





