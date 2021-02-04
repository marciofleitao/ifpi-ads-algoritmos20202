def main():
    senha = 1

    while senha != 2002:
        senha = int(input('Senha: '))
        if senha != 2002:
            print('Senha Invalida')  
        else:
            print('Acesso Permitido') 
            break                     


main()
