def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    inicio = int(dados1[0]) 
    fim = int(dados1[1])

    if inicio < fim:
        tempo = fim - inicio
    else:
        tempo = (24 - inicio) + fim

    print(f'O jogo durou {tempo} hora(s)')



main()
