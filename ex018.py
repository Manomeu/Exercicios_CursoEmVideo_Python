import math
ang = int(input('Digite um angulo para saber sen, cos e tg: '))
ang2 = math.radians(ang)
ang3 = math.degrees(ang)

sen = math.sin(ang2)
cos = math.cos(ang2)
tg = math.tan(ang2)

#pode ser chamado direto um modulo atras do outro
#sen = math.sin(math.radians(ang))
#cos = math.cos(math.radians(ang))
#tg = math.tan(math.radians(ang))


print('=' * 30)
print(f'O angulo de {ang} possui:')
print(f'sen = {sen:.4f}')
print(f'cos = {cos:.4f}')
print(f'tg  = {tg:.4f}')
