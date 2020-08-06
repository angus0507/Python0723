def jpy(func):
    def inner(money):
       money = money / 0.28
       return func(money)
    return inner

def usd(func):
    def inner(money):
       money = money / 30
       return func(money)
    return inner

@jpy
def ecchange(money):
    print(money)

if __name__ == "__main__":
    ecchange(1000)