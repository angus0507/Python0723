def hotDog(func):
    print("我是熱狗")
    return func

def onion(func):
    print("我是洋蔥")
    return func

@hotDog #可以改順序
@onion
def bread():
    print("我是麵包")




if __name__ == "__main__":
    bread()