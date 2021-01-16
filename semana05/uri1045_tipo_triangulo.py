def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    a = float(dados1[0]) 
    b = float(dados1[1])
    c = float(dados1[2]) 
    
    if a >= (b + c):
        print('NAO FORMA TRIANGULO')
    elif (a ** 2) == (b ** 2 + c ** 2):
        print('TRIANGULO RETANGULO')
    elif (a ** 2) > (b ** 2 + c ** 2):
        print('TRIANGULO OBTUSANGULO')
    elif (a ** 2) < (b ** 2 + c ** 2):
        print('TRIANGULO ACUTANGULO')
    elif (a == b == c):
        print('TRIANGULO EQUILATERO')
    elif a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')
    else:
        print('Error')




main()
