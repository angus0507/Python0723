if __name__ == '__main__':
    lev = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
    #       0    1    2    3    4    5    6    7    8    9    10

    dict = {
        "level" : lambda score : print(lev[score//10])
    }

    dict.get('level')(95) #得到A
    dict.get('level')(85) #得到B
    dict.get('level')(75) #得到C
    dict.get('level')(65) #得到D
    dict.get('level')(55) #得到E
    dict.get('level')(25) #得到E
