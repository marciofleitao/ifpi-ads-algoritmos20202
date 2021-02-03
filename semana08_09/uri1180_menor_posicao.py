def main():
    n = int(input('Qtde números: '))
    numeros = input('Números: ')
    numeros = numeros.split()
    for x in range(len(numeros)):
        numeros[x] = int(numeros[x])
    
    menor = numeros[0]
    positions = 0
    for little in range(1, len(numeros)):
        if numeros[little] < menor:
            menor = numeros[little]
            positions = little
    
    print(f'Menor valor: {menor}')
    print(f'Posição: {positions}')


main()


