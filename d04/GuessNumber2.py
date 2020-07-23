import random
import sys
ans = random.randint(0,99)
min, max=0, 100
anount = 50 #可猜 5 次
while anount > 0:

    anount -= 1
    #User猜
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
        print("恭喜使用者答對")
        break

    print("%d~%d之間猜一個數字,按下Enter讓電腦猜...")
    sys.stdin.read(1)
    #電腦猜
    guess = random.randint(min+1, max-1)
    print('電腦在%d~%d之間猜一個數字: %d' %(min,max,guess))
    #是否猜對
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("恭喜電腦答對了")
        break
    #若都沒有猜對
    if anount == 0:
        print("GG了, 答案: %d" %(ans))
