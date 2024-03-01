velocidade = int(input('Qual a velocidade que seu carro se encontra no momento? '))
multa = (velocidade - 80) * 7
print('=' * 30)
if velocidade > 80:
    print('Voce foi multado!')
    print(f'O valor da multa é de {multa} reais')
else:
    print('Esta tudo tranquilho, pode seguir!')
