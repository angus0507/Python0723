import d08.BubbleSort3 as bb
rows =  [
            {'h':170, "w":60},
            {'h':160, "w":55},

        ]
#rows = bb.sort('h', rows)
#rows = bb.sort('w', rows)
# code here...
#根據BMI來排序
for row in rows: #不懂
    w = row.get('w')
    h = row.get('h')
    bmiValue = w/((h/100)**2)
    row.setdefault("bmi", bmiValue)

rows = bb.sort('bmi', row) #不懂
print(rows)

