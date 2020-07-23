date = '170,60&160,48'
# 請算出這二筆 bmi 值各是多少?

for row in date.split('&'):
    print(row, type(row))
    r = row.split(',')
    bmi = '%.2f' % (float(r[1])/(float(r[0])/100)**2)
    print(bmi)