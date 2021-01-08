def main():
    t = int(input('Tempo gasto: '))
    v = int(input('Digite a velocidade: '))

    dist = t*v
    litros = dist/12

    print(f'{litros:.3f}')
    
   
main()