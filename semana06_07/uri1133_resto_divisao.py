def main():
    x = int(input('Número: '))
    y = int(input('Número: '))
    z = x
    if x > y:
        x = y
        y = z
    while x < y:  
        x = x + 1
        if x % 5 == 2 or x % 5 == 3 and x != y:
            print(x)


main()

