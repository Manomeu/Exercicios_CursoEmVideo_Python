valor = 0
while valor == 0:
    sexo = str(input('Digite o sexo da pessoa: [M/F]')).upper().strip()[0]
    if sexo == 'F':
        print('O sexo é feminino')
        break
    elif sexo == 'M':
        print('O sexo é Masculino')
        break
    print('Sexo invalido para esse exercicio, digite de novo!')

########## METODO DO PROFESSOR (MUITO MAIS SIMPLES) ################

sexo = str(input('Digite o sexo da pessoa: [M/F]')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido para esse exercicio, digite o sexo da pessoa: [M/F]')).upper().strip()[0]
if sexo == 'F':
    print('O sexo é feminino')
elif sexo == 'M':
    print('O sexo é Masculino')
