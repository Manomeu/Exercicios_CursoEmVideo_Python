n1 = float(input('\033[40;34mQuantos reais voce tem na carteira? \033[m'))
dolar = n1 / 4.8
print('\033[41;30m=============================================\033[m')
print(f'\033[36mCom esses \033[m\033[97m{n1} \033[36mreais vc pode comprar \033[97m{dolar:.2f} \033[36mdolares.\033[m')
print('\033[31mCotação de R$4,80\033[m')
