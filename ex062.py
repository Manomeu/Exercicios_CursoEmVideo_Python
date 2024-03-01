# print('Programa referente a Progressao aritimetica(PA)')
# t = int(input('Digite o primeiro TERMO da PA: '))
# r = int(input('Digite a RAZAO da PA: '))
# cont = 1
#
# while cont <= 11:
#     if cont != 11:
#         t += r
#         print(t - r)
#         cont += 1
#     else:
#         teste = input('Deseja mais alguns termos? [S/N]').upper()
#         if teste == 'S':
#             cont = 1
#         else:
#             print('Ok, terminamos')

# AO PASSAR O EXERCICIO ELE PEDE PARA MOSTRAR APENAS 10 CASO DESEJE CONTINUAR, NA RESOLIÇÃO ELE MUDA!!!!!!!!##

print('Programa referente a Progressao aritimetica(PA)')
t = int(input('Digite o primeiro TERMO da PA: '))
r = int(input('Digite a RAZAO da PA: '))
cont = 1
total = 0
mais = 10
termos = 0

while mais != 0:
    total += mais
    while cont <= total:
        t += r
        print(t - r, end=' → ')
        cont += 1
    print('PAUSA!')
    mais = int(input('Qantos termos voce deseja a mais? '))
print('FIM!')
print(f'Foram digitados {total} termos.')
