n1 = float(input('\033[30;44mQuantos metros: \033[m'))
km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('\033[41;30m=============================================\033[m')
print('\033[36mkm\033[m', km)
print('\033[36mhm\033[m', hm)
print(f'\033[36mdam \033[m{dam:.2f}')
print('\033[36mdm\033[m', dm)
print('\033[36mCentimetro:\033[m {:.0f}'.format(cm))
print(f'\033[36mMilimetro:\033[m {mm:.0f}')
