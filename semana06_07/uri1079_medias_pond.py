def main():
    n = int(input('Quantidade de números: '))

    for i in range(n):
        numeros = input('Números: ')
        dados = numeros.split()
        n1 = float(dados[0])
        n2 = float(dados[1])
        n3 = float(dados[2])
        num1 = n1*2
        num2 = n2*3
        num3 = n3*5
        media = (num1+num2+num3)/10
        print(f'{media:.1f}')



main()

'''
1080, 1095, 1097, 1099, 1113, 1115, 1117, 1131, 1133, 1142, 1144, 1146, 1150, 1153, 1155, 1157, 1159, 1164
'''