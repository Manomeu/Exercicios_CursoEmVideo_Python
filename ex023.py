numero = str(input('Digite um numero entre 0 e 9999:')).split()
# numero = numero.split()
numero = ''.join(numero)
numero = int(numero)
# Descobrir como bloquear letras

# Matematicamente
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('u', u)
print('d', d)
print('c', c)
print('m', m)


if numero > 9999:
    print('=' * 12)
    print(f'O numero {numero} é maior que 9999')
elif numero < 0:
    print('=' * 12)
    print(f'O numero {numero} é menor que 0')
elif numero > 999 < 9999:
    numero = str(numero)
    print('=' * 12)
    print(f'O numero {numero} é valido:')
    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')
elif numero > 99 < 999:
    numero = str(numero)
    print('=' * 12)
    print(f'O numero {numero} é valido:')
    print(f'Unidade: {numero[2]}')
    print(f'Dezena: {numero[1]}')
    print(f'Centena: {numero[0]}')
    print(f'Milhar: 0')
elif numero > 9 < 99:
    numero = str(numero)
    print('=' * 12)
    print(f'O numero {numero} é valido:')
    print(f'Unidade: {numero[1]}')
    print(f'Dezena: {numero[0]}')
    print(f'Centena: 0')
    print(f'Milhar: 0')
elif numero > -1 < 9:
    numero = str(numero)
    print('=' * 12)
    print(f'O numero {numero} é valido:')
    print(f'Unidade: {numero[0]}')
    print(f'Dezena: 0')
    print(f'Centena: 0')
    print(f'Milhar: 0')
