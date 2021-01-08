def main():
    valor = int(input('Digite um valor: '))
    valor_inicial = valor

    cem = valor//100
    valor = valor%100

    cinq = valor//50
    valor = valor%50

    vinte = valor//20
    valor = valor%20

    dez = valor//10
    valor = valor%10

    cinco = valor//5
    valor = valor%5

    dois = valor//2
    valor = valor%2

    um = valor//1  
    
    print(valor_inicial)
    print(f'{cem} nota(s) de R$ 100,00')
    print(f'{cinq} nota(s) de R$ 50,00')
    print(f'{vinte} nota(s) de R$ 20,00')
    print(f'{dez} nota(s) de R$ 10,00')
    print(f'{cinco} nota(s) de R$ 5,00')
    print(f'{dois} nota(s) de R$ 2,00')
    print(f'{um} nota(s) de R$ 1,00')
    
   
main()
