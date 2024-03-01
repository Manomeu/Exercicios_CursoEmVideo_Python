print('Vamos fazer uma tabuada!')
n = int(input('Digite o numero: '))
print('\033[42;30m====================\033[m')
for i in range(1, 11):
    print(f'{n} X {i:2} =', n*i)
print('\033[42;30m====================\033[m')
