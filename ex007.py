n1 = float(input('\033[46;30mNota do primeiro aluno: \033[m'))
n2 = float(input('\033[40;36mNota do segundo aluno: \033[m'))
media = (n1 + n2) / 2
print('\033[42;30m=============================================\033[m')
print(f'\033[36mA media entre as notas {n1} e {n2} é\033[m', media)
