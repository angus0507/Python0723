def calc(x=1, y=2)->int:

    return x + y

def calc2(x=None, y=None)->int:
    if x == None:
        print("使用者沒有帶入X值")
        return 0
    if y == None:
        print("使用者沒有帶入y值")
        return 0
    return y + x

if __name__ == "__main__":
    sum = calc(10, 20)
    print(sum)
    sum = calc()
    print(sum)
    sum = calc(7)
    print(sum)
    sum = calc(y=7)
    print(sum)

    sum = calc2(6)
    print(sum)
    sum = calc2(y=6)
    print(sum)
    sum = calc2(5, 6)
    print(sum)