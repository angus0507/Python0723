from time import sleep

print('有一棟7層大樓的電梯系統,運作如下: ')
a = 1

while True:


    print("你現在在%d樓,請問要去哪一樓?" %a)
    b = int(input(">>"))
    if b > 7 or b < 1:
        continue

    if a < b :
        print('電梯上樓')

        for i in range(a,b+1):
            print(i)
    if a > b :
        print('電梯下樓')

        for i in range(a,b-1,-1):
            print(i)

    a=b

