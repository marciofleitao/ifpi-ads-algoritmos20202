def main():
    x = y = 1 

    while  x != 0 or y != 0:
        num = input('Coordenadas X e Y: ')
        coord = num.split() 
        x = int(coord[0]) 
        y = int(coord[1]) 
        if (x > 0 and y > 0):
            print("primeiro")
        if (x < 0 and y > 0):
            print("segundo")
        if (x < 0 and y < 0):
            print("terceiro")
        if (x >= 0 and y < 0):
            print("quarto")
        else:
           break


main()


