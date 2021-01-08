def main():
    n = int(input('Digite um valor: '))

    a = n//365
    m = (n%365)//30
    d = (n%365)%30
    
    print(f'{a} ano(s) \n{m} mes(es) \n{d} dia(s)')
    
   
main()

