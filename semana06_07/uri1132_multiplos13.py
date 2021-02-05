def main():
    x = int(input('Número: '))
    y = int(input('Número: '))
    z = 0
    soma = 0
    if x > y:
        x = y
        y = z
    while x <= y:
        if x % 13 != 0:
            soma = soma + x    
        x = x + 1
    print(soma)


main()



