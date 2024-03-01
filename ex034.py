salario = float(input('Qual o seru salario para ganhar um aumento: '))
# codigo novo
if salario > 1250.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print(f'Seu salario aumentou em R${aumento:.2f} e agora vale R${salario + aumento:.2f}')

# código antigo(print retirado de dentro do if)
# if salario > 1250.00:
#     aumento = salario * 0.1
#     print(f'Seu salario aumentou em R${aumento:.2f} e agora vale R${salario + aumento:.2f}')
# else:
#     aumento = salario * 0.15
#     print(f'Seu salario aumentou em R${aumento:.2f} e agora vale R${salario + aumento:.2f}')