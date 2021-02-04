def main():
    x = 1
    y = 2

    while x != y:
        num = input('Números: ')
        numeros = num.split() 
        x = int(numeros[0]) 
        y = int(numeros[1])    

        if x > y:
            print('Decrescente')  
        elif x < y:
            print('Crescente')                      


main()
