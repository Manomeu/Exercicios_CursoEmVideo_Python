print('Programa para verificar se empréstimo será \033[36maprovado\033[m ou \033[31mnegado\033[m')
casa = float(input('Qual o valor da casa que deseja comprar: R$'))
salario = float(input('Qual é o seu salário: R$'))
anos = int(input('Quantos anos voce deseja pagar: '))
meses = anos * 12
parcela = casa / meses
# Simplificado pelo professor
# parcela = casa / (anos * 12)
porcentagem = salario * 0.3

if parcela > porcentagem:
    print('\033[31mSeu empréstimo foi negado!\033[m')
else:
    print('\033[36mSeu empréstimo foi aprovado!\033[m')
    print(f'A prestração da parcela é de R${parcela:.2f}.')

# print('+='*12)
# print('DEBUG:\n'
#       f'Casa: {casa}\n'
#       f'Salario: {salario}\n'
#       f'Anos: {anos}\n'
#       f'Parcela: {parcela}\n'
#       f'Meses: {meses}\n'
#       f'Porcentagem; {porcentagem}')
