def main():
    X = int(input('Distância total percorrida (em Km): '))
    Y = float(input('Total de combustível gasto (em litros): '))

    consumo = X/Y

    print(f'{consumo:.3f} km/l')
    
   
main()