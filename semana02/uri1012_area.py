def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    na = float(dados1[0])
    nb = float(dados1[1])
    nc = float(dados1[2])

    tri_ret = (na*nc)/2
    circ = 3.14159 * (nc**2)
    trap = ((na+nb)*nc)/2
    quad = nb**2
    ret = na*nb

    print(f'TRIANGULO = {tri_ret:.3f} \nCIRCULO = {circ:.3f} \nTRAPÉZIO = {trap:.3f} \nQUADRADO = {quad:.3f} \nRETÂNGULO = {ret:.3f}')


    
main()