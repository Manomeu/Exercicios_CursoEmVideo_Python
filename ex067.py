from time import sleep
n = 0
while True:
    n = int(input('Digite um numero para ver a tabuada: [Negativo para sair] '))
    print('-' * 30)
    if n < 0:
        print('Saindo...')
        sleep(0.5)
        break
    # Professor não utiliza o else, Nao precisa - If apenas para validar saida
    else:
        for i in range(1,11):
            print(f' {i} X {n} = {i * n}')
        print('-' * 30)
print('Tabuada encerrada!')
