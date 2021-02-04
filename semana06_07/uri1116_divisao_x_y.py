def main():
    n = int(input('Número de pares: '))

    for div in range(1, n + 1):
        num = input('Números: ')
        numeros = num.split() 
        x = int(numeros[0]) 
        y = int(numeros[1]) 
        if y == 0:
            print('divisao impossivel')
        elif y != 0:
            divisao = x / y
            print(f'{divisao}')
        else:
            break



main()




