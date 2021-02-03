def main():
    micro = [0,1]
    primeiro = 0
    segundo = 1
    
    for sequencia in range(60):
        seq = primeiro + segundo
        micro.append(seq)
        primeiro = segundo
        segundo = seq
    
    qtde = int(input('Número: '))
    for quantidade in range(qtde):
        val = int(input('Número:'))
        print(f'Fib({val}) = {micro[val]}')
    


main()
