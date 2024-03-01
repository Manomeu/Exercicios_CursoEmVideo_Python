n1 = float(input('Qual a sua primeira nota: '))
n2 = float(input('Qual a sua segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Com a média {media:.1f}, voce foi aprovado!')
elif 6.9 >= media >= 5:
    print(f'Com a média {media:.1f}, voce está em recuperação!')
elif media < 5:
    print(f'Com a média {media:.1f}, voce foi reprovado!')
