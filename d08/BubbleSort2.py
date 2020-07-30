rows = [
        {'age':10, 'score':90},
        {'age':40, 'score':100},
        {'age':20, 'score':80}
        ]
#       0  1  2  3  4

for i in range(0, len(rows)-1):
    for j in range(i+1, len(rows)):
        x = rows[i]
        if rows[i].get('age') > rows[j].get('age'):
            rows[i] = rows[j]
            rows[j] = x


print(rows)