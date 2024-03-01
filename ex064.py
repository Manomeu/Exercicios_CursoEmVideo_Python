soma = 0
cont = 0

while 1:
    n = int(input('Digite um numero e faremos uma soma: (999 - para finalizar!)'))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Apos ter digitado {cont} numeros')
print(f'A soma dos numeros digitados é {soma}')
