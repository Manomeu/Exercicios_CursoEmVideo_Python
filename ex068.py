from random import randint
print('Vamos jogar um jogo de Par ou impar')
print('+=' * 12)
contador = 0
while True:
    computador = randint(0, 10)
    escolha = str(input('Qual a sua opção? [Par/Impar]')).strip().lower()
    n_jogador = int(input('Escolha um numero: '))
    soma = n_jogador + computador
    # Professor utiliza uma unica validação para impar e par, eu estava direncionando em cada um dos IFs
    print(f'Você escolheu {n_jogador} e o computador escolheu {computador}, soma = {soma} - ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'par':
        if soma % 2 == 0:
            print('Ganhou!')
            contador += 1
        else:
            print('Perdeu!')
            break
    elif escolha == 'impar':
        if soma % 2 != 0:
            print('Ganhou!')
            contador += 1
        else:
            print('Perdeu!')
            break
    else:
        print('Opção inválida, tente novamente!')
print('+=' * 12)
print(f'Game Over!, ganhou um total de {contador} vezes consecutivas.')

# professor utiliza um While para validar PAR ou Impar
# par_ou_impar = ''
# while par_ou_impar not in 'PI':
#     par_ou_impar = str(input('Qual a sua opção? [Par/Impar]')).strip().upper()
