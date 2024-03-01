soma = cont = 0
while True:
    n = int(input('Digite um numero [999 - parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} numero digitados é {soma}.')





