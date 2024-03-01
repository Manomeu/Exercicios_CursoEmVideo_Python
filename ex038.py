primeiro = int(input('Digite o primeiro numero: '))
segundo = int(input('Digite o segundo numero: '))

if primeiro > segundo:
    print(f'O primeiro numero é maior! {primeiro} > {segundo}')
elif segundo > primeiro:
    print(f'O segundo numero é maior! {segundo} > {primeiro}')
elif primeiro == segundo:
    print(f'Os numeros são iguais! {primeiro} = {segundo}')

# Podemos usar apenas "else:" para a terceira opção