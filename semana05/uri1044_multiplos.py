def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    a = int(dados1[0]) 
    b = int(dados1[1]) 
    
    if a < b and b % a == 0:
        print('São múltiplos')
    elif a > b and a % b == 0:
        print('São múltiplos')
    elif a < b and b % a != 0:
        print('Não são múltiplos')
    elif a > b and a % b != 0:
        print('Não são múltiplos')
    else:
        print('Error')



main()
