users = [
            {'name':'John', "h":170, 'w':60},
            {'name':'Mary', "h":160, 'w':48}
        ]
#請計算每一筆的BMI值
for user in users:
    h = user.get("h")
    w = user.get("w")
    bmi = "%.2f" % (w/((h/100)**2))
    print(user, type(user), h, w, bmi)
