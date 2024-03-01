peso = float(input('Qual o seu peso: (Kg) '))
altura = float(input('Qual a sua altura: (m) '))
imc = peso / altura ** 2
print('DEBUG: ', imc)
if imc < 18.5:
    print(f'Com seu imc em {imc:.2f}, voce está na magreza!')
elif imc <= 25:
    print(f'Com seu imc em {imc:.2f}, voce está no peso ideal!')
elif imc <= 30:
    print(f'Com seu imc em {imc:.2f}, voce está com sobrepeso!')
elif imc <= 40:
    print(f'Com seu imc em {imc:.2f}, voce está obeso!')
else:
    print(f'Com seu imc em {imc:.2f}, voce está com obesidade mórbida!')


