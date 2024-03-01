print('-' * 30)
print('     CADASTRO DE PESSOAS')
print('-' * 30)
mais_desoito = masculino = feminino_menor = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    if idade >= 18:
        mais_desoito += 1
# Valida se sexo é M ou F, caso não, continua repetindo a pergunta.
# while sexo not in 'mf':
#     if sexo in 'mf':
#         if sexo == 'm':
#             break
#         elif sexo == 'f':
#             break
#     else:
#         sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
###########
# Simplificado pelo professor, Não precisa fazer a validação com os IFs
# (Persebido por mim que a validação dos IFs nem ocorre.)
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    print('-' * 30)
    if sexo == 'm':
        masculino += 1
    if sexo == 'f' and idade < 20:
        feminino_menor += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
# Valida se continuar é S ou N, caso não, continua repetindo a pergunta.
# while continuar not in 'sn':
#     if continuar in 'sn':
#         if continuar == 's':
#             print('-' * 30)
#             print('     CADASTRO DE PESSOAS')
#             print('-' * 30)
#             break
#         elif continuar == 'n':
#             break
#     else:
#         continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
#############
# Novamente sem validações dos Ifs
# (Persebido por mim que a validação dos IFs nem ocorre.)
    while continuar not in 'sn':
            continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
# print('=+' * 13 + 'RESULTADO' + '=+' * 13)
print(f'{'RESULTADO':-^60}')
print(f'{mais_desoito} pessoa(s) tem mais de 18 anos.')
print(f'{masculino} homem(ns) foi(ram) cadastrado(s).')
print(f'{feminino_menor} mulher(es) com menos de 20 anos foi(ram) cadastrada(s).')
print('=+' * 30)
