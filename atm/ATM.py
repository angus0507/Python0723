import os
import atm.Account as act
#主程式

act1 = act.Account(1000)
act2 = act.Account(1000)
act3 = act.Account(1000)
list = [{"john": act1}, {"merry": act2}, {"tom": act3}]

# 列出所有人的帳戶餘額
def display():
    for act in list:
        for key in act.keys():
            print(key, act.get(key))

def save():
    actName = input("請輸入存款人")
    x = int(input("請輸入存款金額"))
    #得到存款人的 account 物件
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print("查無此人")
    else:
        account.save(x)


def wirthdraw():
    actName = input("請輸入提款人")
    x = int(input("請輸入提款金額"))
    #得到提款人的 account 物件
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print("查無此人")
    else:
        account.withdraw(x)

def transfer():
    fromName = input("請輸入轉帳人(from): ")
    toName = input("請輸入被轉帳人(to): ")
    x = int(input("請輸入轉帳金額"))
    fromAccount = None
    toAccount = None
    for act in list:
        for key in act.keys():
            if key == fromName:
                fromAccount = act.get(key)
            if key == toName:
                toAccount = act.get(key)
    if fromAccount == None or toAccount == None:
        print("查無此人")
    else:
        fromAccount.transfer(x, toAccount)

def createAccount():
    acconutName = input("請輸入開戶名稱: ")
    x = int(input("請輸入開戶金額: $"))
    acconut = act.Account(x)
    dict = {acconutName: acconut}
    list.append(dict)

def cancelAccount():
    cancelName = input("請輸入解約人 ")
    createDict = None
    for dict in list:
        for key in dict.keys():
            if key == cancelName:
                 createDict = dict
    if createDict == None:
        print("查無此人")
    else:
        list.remove(createDict)
        createAccount = createDict.get(cancelName)
        print("解約人: " + cancelName +',解約金: ' + str(createAccount.getMoney()))



#系統選單
while True:
    print("系統選單")
    print("----------")
    print("1. 查詢")
    print("2. 存款")
    print("3. 提款")
    print("4. 轉帳")
    print("5. 開戶")
    print("6. 解約")
    print("9. 離開")
    no = int(input("請選擇(1~9) "))
    if no == 1:
        display()
    elif no == 2:
        save()
    elif no == 3:
        wirthdraw()
    elif no == 4:
        transfer()
    elif no == 5:
        createAccount()
    elif no == 6:
        cancelAccount()
    elif no == 9:

        break

    os.system("pause") # 暫停(按下任意見後繼續...)

print("程式結束")



