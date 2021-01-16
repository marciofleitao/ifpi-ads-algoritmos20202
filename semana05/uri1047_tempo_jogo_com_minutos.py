def main():
    num = input('Informe os números: ')

    dados1 = num.split()
    hora_i = int(dados1[0]) 
    min_i = int(dados1[1])
    hora_f = int(dados1[2])
    min_f = int(dados1[3])

    if hora_i < hora_f:
        hora = hora_f - hora_i
        if min_i < min_f:
            minuto = min_f - min_i
        elif min_i > min_f:
            hora = hora - 1
            minuto = (60 - min_i) + min_f
        elif min_i == min_f:
            minuto = 0
        else:
            ('Error')
    if hora_i > hora_f:
        hora = (24 - hora_i) + hora_f
        if min_i < min_f:
            minuto = min_f - min_i
        elif min_i > min_f:
            hora = hora - 1
            minuto = (60 - min_i) + min_f
        elif min_i == min_f:
            minuto = 0
        else:
            ('Error')
    if hora_i == hora_f:
        if min_i < min_f:
            minuto = min_f - min_i
            hora = 0
        elif min_i > min_f:
            minuto = (60 - min_i) + min_f
            hora = 23
        elif min_i == min_f:
            hora = 24
            minuto = 0
        else:
            ('Error')


    print(f'O jogo durou {hora} hora(s) e {minuto} minuto(s)')

main()



