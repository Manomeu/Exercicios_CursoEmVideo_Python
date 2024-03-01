print('Programa referente a Progressao aritimetica(PA)')
t = int(input('Digite o primeiro TERMO da PA: '))
r = int(input('Digite a RAZAO da PA: '))
cont = 1

while cont <= 10:
    t += r
    print(t - r, end=' → ')
    cont += 1
print('FIM!')
