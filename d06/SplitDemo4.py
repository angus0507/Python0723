date = 'orange=10,apple=30,berry=20'
#將字串變成字典dict格式
fruits = dict(item.split('=')for item in date.split(','))
print(fruits)
print(fruits.get('apple'))
