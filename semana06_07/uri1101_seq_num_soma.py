
def main():
    soma = 0
    zero = 0

    while zero != 1:
        num = input('Números: ')
        numeros = num.split() 
        n1 = int(numeros[0]) 
        n2 = int(numeros[1]) 
        soma = 0
        if n1 > n2:
            naux = n1
            n1 = n2
            n2 = naux
        if n1 <= 0 or n2 <= 0:
            zero = 1
        if zero != 1:
            for somar in range(n1, n2+1):
                print(f'{somar}')
                soma = soma + somar
                if somar == n2:
                    print(f'Sum={soma}')     



main()
