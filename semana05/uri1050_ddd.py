def main():
    ddd = int(input('Informe o ddd: '))

    if ddd == 61:
        cidade = 'Brasilia'
    elif ddd == 71:
        cidade = 'Salvador'
    elif ddd == 11:
        cidade = 'Sao Paulo'
    elif ddd == 21:
        cidade = 'Rio de Janeiro'
    elif ddd == 32:
        cidade = 'Juiz de Fora'
    elif ddd == 19:
        cidade = 'Campinas'
    elif ddd == 27:
        cidade = 'Vitoria'
    elif ddd == 31:
        cidade = 'Belo Horizonte'
    elif ddd == 86:
        cidade = 'Teresina'
    else:
        cidade = 'DDD não cadastrado'
    
    print(f'{cidade}')




main()