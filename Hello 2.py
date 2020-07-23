h=int(input('請輸入身高'))
w=int(input('請輸入體重'))
bmi=w/(h/100)**2
print(bmi)
if 18 <=bmi <23:
    print("正常")
if bmi >=23:
    print("過胖")
if bmi <18:
    print("過瘦")

