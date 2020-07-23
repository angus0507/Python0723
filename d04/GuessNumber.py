import random
ans = random.randint(0,99)
min, max=0, 100
anount = 5 #可猜 5 次
while anount > 0:

    anount -= 1
    guess = int(input("請在%d~%d之間猜一個數字: " % (min,max)))

    #驗證範圍
    if guess <= min or guess >= max:
        print("輸入範圍錯誤,請重新輸入")
        continue
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("恭喜答對")
        break


    #若都沒有猜對
    if anount == 0:
        print("GG了, 答案: %d" %(ans))
