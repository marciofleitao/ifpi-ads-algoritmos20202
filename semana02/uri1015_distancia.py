def main():
    x1 = float(input('Digite um número: '))
    y1 = float(input('Digite um número: '))
    x2 = float(input('Digite um número: '))
    y2 = float(input('Digite um número: '))


    dist = (((x2 - x1)**2)+((y2-y1)**2))**0.5

    print(f'{dist:.4f}')
    
   
main()