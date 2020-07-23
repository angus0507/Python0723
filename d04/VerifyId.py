#
def areaNum(area):
    if area == "A":
        return "10"
    if area == "B":
        return "11"
    if area == "C":
        return "12"
    if area == "D":
        return "13"
    if area == "E":
        return "14"
    if area == "F":
        return "15"
    if area == "G":
        return "16"
    if area == "H":
        return ""
    if area == "I":
        return ""
    if area == "J":
        return ""
    if area == "K":
        return ""
    if area == "M":
        return ""
    if area == "N":
        return ""
    if area == "O":
        return ""
    if area == "P":
        return ""
    if area == "Q":
        return ""
    if area == "P":
        return ""



#驗證身份證字號
def verifyId(id):

    id2 = areaNum(id[0])+id[1] +id[2] + id[3] + id[4] + id[5] + id[6]+ id[7]+ id[8] + id[9]
    delta = "19876543211"
    print(id)
    print(id2)
    print(delta)

    sum = int(id2[0])*int(delta[0])+\
        int(id2[1])*int(delta[1])+\
         int(id2[2])*int(delta[2])+\
         int(id2[3])*int(delta[3])+\
         int(id2[4])*int(delta[4])+\
          int(id2[5])*int(delta[5])+\
          int(id2[6])*int(delta[6])+\
          int(id2[7])*int(delta[7])+\
          int(id2[8])*int(delta[8])+\
          int(id2[9])*int(delta[9])+\
          int(id2[10])*int(delta[10])
    print(sum)
    print('正確' if sum % 10 == 0 else "錯誤")

#主程式
id = input("請輸入身分證字號: ")
verifyId(id)