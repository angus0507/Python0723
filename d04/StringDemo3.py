report = "台積電目前價格每股300元,非常適合買進"
amount = 1000 #想買 1000 股(一張)
cost = 0 #
price = report[9:12]#不含第12個字元
print(price, type(price))
cost = amount*int(price)#請算出買進成本
print(cost)