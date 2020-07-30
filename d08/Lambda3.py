exchang = {
    'usd' : lambda money : print(money / 30),
    'jpy' : lambda money : print(money * 4)
}

exchang.get('usd')(900)
exchang.get('jpy')(900)