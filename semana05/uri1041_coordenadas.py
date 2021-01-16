def main():
    x = float(input('Informe o x: '))
    y = float(input('Informe o y: '))


    if x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y < 0:
        print('Q4')
    elif x == 0 and y == 0:
        print('Origem')
    else:
        print('Error')

        
        


main()

