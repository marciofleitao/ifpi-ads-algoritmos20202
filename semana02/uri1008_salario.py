def main():
    n_func = int(input('Digite o número do funcionário: '))
    h_trab = int(input('Informe a quantidade de horas trabalhadas: '))
    valor_h = float(input('Digite o valor recebido por hora: '))
    
    salario = h_trab*valor_h

    print(f'NUMBER = {n_func} \nSALARY = U$ {salario:.2f}')
    

main()