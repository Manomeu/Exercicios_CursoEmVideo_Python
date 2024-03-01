soma = 0
contador = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        contador += 1
print(f'A soma dos {contador} numeros impares e divisiveis por 3 entre 1 e 500 é:', soma)

# for contando direto numeros impares (MENOS PROCESSAMENTO)
# for i in range(1, 500, 2):
#     if i % 3 == 0:
#         soma += i
#         contador += 1
# print(f'A soma dos {contador} numeros impares e divisiveis por 3 entre 1 e 500 é:', soma)