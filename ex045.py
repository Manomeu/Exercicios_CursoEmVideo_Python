# JOKENPO
# Iniciando jogo
print('\33[31mIniciaremos o Jokenpo.\33[m\n\33[36mTente ganhar do computador!\33[m')

# PC
from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
pc = choice(opcoes)

print('=+' * 12)
# PLAYER
player = str(input('Escolha o que jogar (Pedra, Papel e Tesoura):')).strip().lower()

# carregando resultado
import time

print('PEDRA')
time.sleep(1)
print('PAPEL')
time.sleep(1)
print('TESOUUUUURA')
time.sleep(1)

print('=+'*30)
# Resultados
# EMPATE
if pc == 'tesoura' and player == 'tesoura' or pc == 'pedra' and player == 'pedra' or pc == 'papel' and player == 'papel':
    print(f'PC = {pc}\nPlayer = {player}')
    print('=+' * 30)
    print('EMPATE!')
# DERROTA
elif pc == 'tesoura' and player == 'papel' or pc == 'pedra' and player == 'tesoura' or pc == 'papel' and player == 'pedra':
    print(f'PC = {pc}\nPlayer = {player}')
    print(f'\33[31m{pc} ganha de {player}\33[m')
    print('=+' * 30)
    print('Voce perdeu! Computador Wins!!!')
# VITORIA
elif pc == 'tesoura' and player == 'pedra' or pc == 'pedra' and player == 'papel' or pc == 'papel' and player == 'tesoura':
    print(f'PC = {pc}\nPlayer = {player}')
    print(f'\33[36m{player} ganha de {pc}\33[m')
    print('=+' * 30)
    print('Voce ganhou! Parabens!!!!!')

# Professor fez as opções aninhada
# if pc = pedra
#    if jogador = pedra
#         empate
#    elif jogador = tesoura
#         pc ganha
#    elif jogador = papel
#         jogador ganha
# elif pc = tesoura
#     if jogador = pedra
#       jogador ganha
#     elif jogador = tesoura
#       empate
#     elif jogador = papel
#       pc ganha
# elif pc = papel
#     if jogador = pedra
#       pc ganha
#     elif jogador = tesoura
#       jogador ganha
#     elif jogador = papel
#       empate
