def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    cod = int(dados1[0])
    qtd = int(dados1[1])

    if cod == 1:
        total = qtd * 4
        print(f'Total: R$ {total:.2f}')
    elif cod == 2:
        total = qtd * 4.5
        print(f'Total: R$ {total:.2f}')
    elif cod == 3:
        total = qtd * 5
        print(f'Total: R$ {total:.2f}')
    elif cod == 4:
        total = qtd * 2
        print(f'Total: R$ {total:.2f}')
    elif cod == 5:
        total = qtd * 1.5
        print(f'Total: R$ {total:.2f}')
    else:
        print('Error')



    
main()