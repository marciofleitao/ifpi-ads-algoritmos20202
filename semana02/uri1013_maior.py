def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    na = int(dados1[0])
    nb = int(dados1[1])
    nc = int(dados1[2])

    maiorab = (na+nb+abs(na-nb))/2
    maiorabc = (maiorab+nc+abs(maiorab-nc))/2
    maior = int(maiorabc)


    print(f'{maior} eh o maior')


    
main()