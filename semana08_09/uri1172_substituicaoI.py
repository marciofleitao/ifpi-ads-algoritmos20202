def main():
    for i in range(10):
        valor = int(input('Número: '))
        if valor < 1:
            valor = 1
        print(f'X[{i}] = {valor}')



main()