def main():
    soma = 0
    qtde = 0
    while qtde < 2:
        nota = float(input('Nota: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            qtde = qtde + 1
        else:
            print('nota invalida')
    soma = soma/2
    print(f'media={soma:.2f}')

main()




