def main():
    sal = float(input('Informe o salário: '))

    if sal >= 0.0 and sal <= 400.00:
        porcentagem = 15
        reajuste = (sal * porcentagem) / 100 
        novo_salario = sal + reajuste
    elif sal >= 400.01 and sal <= 800.00:
        porcentagem = 12
        reajuste = (sal * porcentagem) / 100 
        novo_salario = sal + reajuste
    elif sal >= 800.01 and sal <= 1200.00:
        porcentagem = 10
        reajuste = (sal * porcentagem) / 100 
        novo_salario = sal + reajuste
    elif sal >= 1200.01 and sal <= 2000.00:
        porcentagem = 7
        reajuste = (sal * porcentagem) / 100 
        novo_salario = sal + reajuste
    elif sal > 2000.00:
        porcentagem = 4
        reajuste = (sal * porcentagem) / 100 
        novo_salario = sal + reajuste
    else:
        ('Error')

    print(f'Novo salario: {novo_salario:.2f} \nReajuste ganho: {reajuste:.2f} \nEm percentual: {porcentagem} %')



main()