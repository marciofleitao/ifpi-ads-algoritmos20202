def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    n1 = float(dados1[0]) 
    n2 = float(dados1[1]) 
    n3 = float(dados1[2]) 

    if abs(n2 - n3) < n1 < (n2 + n3) and (n1 - n3) < n2 < (n1 + n3) and (n1 - n2) < n3 < (n1 + n2):
        perimetro = n1 + n2 + n3
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area = ((n1 + n2) * n3) / 2
        print(f'Area = {area:.1f}')



main()
