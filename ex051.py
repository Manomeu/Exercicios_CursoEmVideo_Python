print('Programa referente a Progressao aritimetica(PA)')
t = int(input('Digite o primeiro TERMO da PA: '))
r = int(input('Digite a RAZAO da PA: '))

for i in range(0, 10):
        t += r
        print(t - r)

# metodo do professor
# acrecenta uma variavel referente ao decimo termo, for com todos as variaveis.
# decimo = t + (10 - 1) * r
#
# for i in range(t, decimo + r, r):
#         print(i)









# PA = (a1,a2,a3,a4,...,aN)
# a1 = a1
# a2 = a1 + 1.r
# a3 = a1 + 2.r
# a4 = a1 + 2.r
# aN = a1 + (n-1).r
