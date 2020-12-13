def main():
    n_func = str(input('Digite o nome do funcionário: '))
    sal_fix = float(input('Digite o valor do salário fixo: '))
    valor_v = float(input('Digite o total de vendas efetuadas por ele no mês (em dinheiro): '))
    
    salario_f = sal_fix + (valor_v*0.15)

    print(f'TOTAL = {salario_f:.2f}')
    

main()