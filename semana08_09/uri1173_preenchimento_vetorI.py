def main():
    val = int(input('Número: '))
    print(f'N[0] = {val}')
    for i in range(1,10):
        val = val * 2
        print(f'N[{i}] = {val}')



main()
