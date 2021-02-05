def main():
    n = int(input('Número: '))
    x = 1
    for seq in range(1,(n*2)+1):
        if seq % 2 == 0: 
            print(f'{x} {x ** 2 + 1} {x ** 3 + 1}')
            x = x + 1
        else:
            print(f'{x} {x ** 2} {x ** 3}')              

    
main()