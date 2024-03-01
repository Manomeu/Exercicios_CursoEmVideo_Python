n = int(input('Digite um numero e saberemos a sequencia em fibonachi: '))
a = 0
b = 1
cont = 0
fibo = 0

while cont <= n:
    if cont < n:
        print(a, end=' ')
        fibo = a + b
        a = b
        b = fibo
        cont += 1
    elif cont == n - 1:
        print(a)


