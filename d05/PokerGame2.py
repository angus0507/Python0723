import random
import time

def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return p  # 2~10的數字

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
random.shuffle(poker)  # 洗牌
print(poker)

# 牌局開始先發一張
p1 = poker.pop()
sum = getScore(p1)
print('已拿:', p1, '總分:', sum)
print('剩餘:', poker)

# 繼續拿牌 ?
count_user = 0;
while True:
    ask = input('是否要拿牌(y/n)? ')
    if ask == 'y':
        p = poker.pop()
        sum += getScore(p)
        print('再拿:', p, '總分:', sum)
        if sum > 10.5:
            print('User 爆了')
            break
        else:
            count_user += 1
        if count_user == 5:
            print('User 過五關, 超強的~~~')
            break
    else:
        break

# PC 拿牌
count_pc = 0
p2 = poker.pop()
sum2 = getScore(p2)
print('PC已拿:', p2, '總分:', sum2)
print('剩餘:', poker)

while True:
    take = False  # 是否拿牌?
    time.sleep(2)  # 延遲 2 秒
    if sum2 >= 9:  # 電腦若為 9 點（含）以上不需補牌
        break
    elif sum2 < 7: # 電腦少於 7 點點需強迫補牌
        take = True
    elif sum2 == 7 or sum2 == 7.5:
        amount = poker.count('A') + poker.count(2) + poker.count(3)
        if amount >= 10:
            take = True
    elif sum2 == 8 or sum2 == 8.5:
        amount = poker.count('A') + poker.count(2)
        if amount >= 7:
            take = True

    # 是否拿牌 ?
    if take:
        p = poker.pop()
        sum2 += getScore(p)
        print('PC再拿:', p, '總分:', sum2)

    # 判斷是否爆了 ?
    if sum2 > 10.5:
        print('PC 爆了')
        break
    else:
        count_pc += 1

    # 判斷是否過五關 ?
    if count_pc == 5:
        print('PC 過五關, 超強的~~~')
        break