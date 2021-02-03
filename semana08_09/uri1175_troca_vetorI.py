def main():
    lista = []
    for valor in range(20):
        val = int(input('Número: '))
        lista.append(val)
    positions = 0
    for numeros in lista[::-1]:
        print(f'N[{positions}] = {numeros}')
        positions = positions + 1


main()

