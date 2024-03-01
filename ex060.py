from math import factorial

n = int(input('Digite um numero e descobriremos seu fatorial: '))
fatorialw = 1
fatorialf = 1
fatorialprof = 1
contador = 1
c = n
## While do professor
print(f'O Fatorial pelo Professor: {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' X ' if c > 1 else ' = ', end='')
    fatorialprof *= c
    c -= 1
print(fatorialprof)

# while funcionando
# crio uma variavel contador para funcionar igual a range no for.
while contador <= n:
    fatorialw = fatorialw * contador
    contador += 1
print(f'O Fatorial pelo While é: {fatorialw}')

# For funcionando
for i in range(n, 1, -1):
    fatorialf = fatorialf * i
print(f'O Fatorial pelo FOR é: {fatorialf}')

# Factorial funcionando
f = factorial(n)
print(f'O Fatorial pelo Factorial é: {f}')

###### Professor utiliza from math import factorial
