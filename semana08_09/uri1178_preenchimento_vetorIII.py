def main():
    x = float(input('Número: '))
    for i in range(0,100):
        print(f'N[{i}] = {x:.4f}')
        x = x / 2 
        

main()

