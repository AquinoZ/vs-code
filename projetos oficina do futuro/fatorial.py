
while True:
    numero = int(input('digite: '))
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
        if numero == 0:
            print(1)
        else:
            print(fatorial)
    dnv = input('tentar novamente? (S p/ SIM) (N p/ NÃO)')
    if dnv == 'N':
        break

