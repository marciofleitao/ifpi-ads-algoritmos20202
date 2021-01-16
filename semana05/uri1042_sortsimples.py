def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    n1 = int(dados1[0])
    n2 = int(dados1[1])
    n3 = int(dados1[2])

    maior = mai(n1, n2, n3)
    inter = inte(n1, n2, n3)
    menor = men(n1, n2, n3)
    print(f'{menor} \n{inter} \n{maior}\n')
    print(f'{n1} \n{n2} \n{n3}')


def mai(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3


def inte(n1, n2, n3):
    if (n1<=n2 and n1>=n3) or (n1>=n2 and n1<=n3):
        return n1
    elif (n2<=n1 and n2>=n3) or (n2>=n1 and n2<=n3):
        return n2
    else:
        return n3


def men(n1, n2, n3):
    if n1<=n2 and n1<=n3:
        return n1
    elif n2<=n1 and n2<=n3:
        return n2
    else:
        return n3

        
        
main()

