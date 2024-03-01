from time import sleep
soma = cont = media = maior = menor = 0

while 1:
    n = int(input('Digite um numero: '))
    if cont == 0:
        maior = n
        menor = n
        cont += 1
        soma += n
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar == 'N':
            break
        else:
            print('Esntão vamos continuar!')
            sleep(0.5)
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
        cont += 1
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar == 'N':
            break
        else:
            print('Esntão vamos continuar!')
            sleep(0.5)
media = soma / cont
print(f'A media dos {cont} numeros digitados é {media}!')
print(f'Maior numero é {maior}')
print(f'Menor numero é {menor}')

### Professor inicia o whili:
# resposta = 'S'
# while resposta in 'Ss'

