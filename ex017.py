import math
cata = float(input('Qual o comprimento do cateto adjacente: '))
cato = float(input('Qual o comprimento do cateto oposto: '))
# teste1 = (cato ** 2) + (cata ** 2)
# hipo_teste1 = math.sqrt(teste)

# hipo_teste2 = ((cato ** 2) + (cata ** 2)) ** 0.5

hipo = math.hypot(cata, cato)

print(f'O comprimento da hipotenusa é {hipo:.2f}')
