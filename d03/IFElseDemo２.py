def BMI(h, w):
    bmi = w / ((h/100)**2)
    if(bmi > 23):
        result = "過重"
    elif(bmi < 18):
        result = "過輕"
    else:
        result =  "正常"
    return bmi, result, h, w

