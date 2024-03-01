frase = str(input('Vamos descobrir se sua frase é um palindromo, DIGITE: ')).lower().strip().split()
print('+=' * 15, 'SEM FOR', '+=' * 15)
normal = ''.join(frase)
contra = ''.join(frase)[::-1]

if normal == contra:
    print(f'A frase ({normal}) é um palindromo! ({contra})')
elif normal != contra:
    print(f'A frase ({normal}) não é um palindromo! ({contra})')

###############################
print('+=' * 15, 'COM FOR', '+=' * 15)
# Com for pq é o motivo da aula
inverso = ''
for i in range(len(normal) -1, -1, -1):
    inverso += normal[i]
if normal == inverso:
    print(f'A frase ({normal}) é um palindromo! ({inverso})')
elif normal != inverso:
    print(f'A frase ({normal}) não é um palindromo! ({inverso})')