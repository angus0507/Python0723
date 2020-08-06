import util.TWII as t

#pe(本益比), dy(殖利率), pb(股價淨值比)
rows = t.analysys(10, 7, 1)
print(rows)
stock = t.getProductByname("鴻海")
print(stock)