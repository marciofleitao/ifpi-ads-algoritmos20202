def main():
    n1 = float(input('Informe o número: '))
    n2 = float(input('Informe o número: '))
    n3 = float(input('Informe o número: '))
    n4 = float(input('Informe o número: '))

    media = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10

    if media >= 7.0:
        print(f'\nMedia:{media:.1f}\nAluno aprovado.')
    elif media >= 5.0 and media <= 6.9:
        nota_exame = float(input('Nota do exame:'))
        media_exame = (nota_exame+media)/2
        if media_exame >=5.0:
            (print(f'\nMedia: {media:.1f}\nAluno em exame. \nNota no exame: {nota_exame:.1f} \nAluno aprovado. \nMedia final: {media_exame:.1f}'))
        else:
            (print(f'\nMedia: {media:.1f}\nAluno em exame. \nNota no exame: {nota_exame:.1f} \nAluno reprovado. \nMedia final: {media_exame:.1f}'))
    elif media < 5.0:
        print(f'\nMedia:{media:.1f}\nAluno reprovado.')
    else:
        print('Error')

        
        


main()

