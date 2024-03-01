n1 = int(input('\033[40;36mInforme um número: \033[m'))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** 0.5
print('\033[40;31m=============================================\033[m')
print('\033[36mO dobro, triplo e raiz quadrada do número {} são {}, {} e {:.2f} respectivamente.\033[m'.format(n1, dobro, triplo, raiz))
