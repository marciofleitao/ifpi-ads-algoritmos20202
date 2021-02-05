def main():
    valor = int(input('Valor: '))
    alcool = 0
    gasolina = 0
    diesel = 0
    while valor != 0:
        valor = int(input('Valor: '))
        if valor == 1:
            alcool = alcool + 1
        if valor == 2:
            gasolina = gasolina + 1
        if valor == 3:
            diesel = diesel + 1
    print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')


main()

