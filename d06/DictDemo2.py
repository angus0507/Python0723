users = {'John':[170, 60], 'Mary':[160, 48]}
names = users.keys()
for name in names:
    h = float(users.get(name)[0])
    w = float(users.get(name)[1])
    bmi = w / ((h/100)**2)
    print(name, users.get(name), h, w,('%.2f'%bmi))