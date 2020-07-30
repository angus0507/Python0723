def sort(key, rows):  # key 欄位, rows 資料源
    for i in range(0, len(rows) - 1):
        for j in range(i + 1, len(rows)):
            x = rows[i]
            if rows[i].get(key) > rows[j].get(key):
                rows[i] = rows[j]
                rows[j] = x
    return rows



if __name__ == "__main__":
    rows = [
        {'age': 10, 'score': 90},
        {'age': 40, 'score': 100},
        {'age': 20, 'score': 80}
    ]

    rows = sort('age', rows)
    print(rows)

    rowss = sort('score', rows)
    print(rows)