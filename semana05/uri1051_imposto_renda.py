def main():
    sal = float(input('Informe o salário: '))

    if sal >= 0.0 and sal <= 2000.00:
        print('Isento')
    elif sal >= 2000.01 and sal <= 3000.00:
        imp = (2000.00 - sal) * (8 / 100)
        print(f'R$ {imp:.2f}')
    elif sal >= 3000.01 and sal <= 4500.00:
        imp = ((sal - 3000.00) * (18 / 100)) + ((8 / 100) * 1000.00)
        print(f'R$ {imp:.2f}')
    elif sal > 4500.00:
        imp = ((sal - 4500.00) * (28 / 100)) + ((8 / 100) * 1000.00) + ((18 / 100) * 1500.00)
        print(f'R$ {imp:.2f}')
    else:
        print('Error')



main()