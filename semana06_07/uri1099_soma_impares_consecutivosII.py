def main():
    n = int(input('Número: '))
    z = 0

    for soma in range(1, n + 1):
        num = input('Números: ')
        numeros = num.split() 
        n1 = int(numeros[0]) 
        n2 = int(numeros[1]) 
        x = 0

        if n1 > n2:
            for z in range(int(numeros[1]) + 1, int(numeros[0])):
                if z % 2 != 0:
                    x = x + z
        if n1 < n2:
            for z in range(int(numeros[0])+ 1, int(numeros[1])):
                if z % 2 != 0:
                    x = x + z
        if n1 == n2:
            x = 0
        print(x)



main()
