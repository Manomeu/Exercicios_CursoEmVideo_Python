reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta2 + reta1):
    print('É possivel criar um triangulo e:')
    if reta1 == reta2 == reta3:
        print('Esse é um triangulo equilátero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse é um triangulo isósceles!')
    else:
        print('Esse é um triangulo escaleno!')
else:
    print('Não é possivel criar um triangulo.')
