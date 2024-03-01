numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
validador = True
while validador:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'Voce escolheu o numero', numeros_por_extenso[numero])
        break
    else:
        print('Número invalido! ', end='')
