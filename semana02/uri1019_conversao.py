def main():
    n = int(input('Digite um valor: '))

    h = n//3600
    m = (n%3600)//60
    s = (n%3600)%60
    
    print(f'{h}:{m}:{s}')
    
   
main()