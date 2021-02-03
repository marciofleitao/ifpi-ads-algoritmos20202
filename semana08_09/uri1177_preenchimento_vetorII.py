def main():
    t = int(input('Número: '))
    lista = []
    l = 0
    tezao = 0

    while tezao < 1000:
        lista.append(l)
        print(f'N[{tezao}] = {l}')
        if l < (t - 1):
            l = l + 1
        else:
            l == t - 1
            l = 0
        tezao = tezao + 1
        


main()
