def calc(x,y):#自解
    rabbit = (y-(2*x))/2
    chicker=(x-rabbit)
    return chicker, rabbit

chicker, rabbit = calc(83,240)
print("雞:%d 兔:%d" % (chicker, rabbit))

def calc(x,y):
    a = 2 * x
    b = y - a
    rabbit = b / 2
    return x-rabbit , rabbit


chicker, rabbit = calc(83,240)
print("雞:%d 兔:%d 隻數:%d 腳數:%d" % (chicker, rabbit,chicker+rabbit,(chicker*2+rabbit*4)))
