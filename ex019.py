import random
nome1 = 'Gabriella'
nome2 = 'Matheus'
nome3 = 'Laura'
nome4 = 'Clara'
nome5 = 'Betinha'
lista = [nome1, nome2, nome3, nome4, nome5]
print('Um dos alunos abaixo será escolhido para apagar o quadro:')
print(nome1)
print(nome2)
print(nome3)
print(nome4)
print(nome5)
print('=' * 12)
print('O nome escolhido foi:', random.choice(lista))
