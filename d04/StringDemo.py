word = "she sell sea shell on the sea shore"
print(word.count('s'))
print(word.count('she'))
print(word.count(' '))

password = "abcABC123".join("abc")
print(password)
print(len(password))
print(password.isalpha())#是否包含英文文字
print(password.isalnum())#是否包含英文或數字
print(password.isdigit())#是否包含數字

str = 'Hello python'#0開始算
print(str[4])
# Hello python
# 0123456789...
print(str[-4])
print(str[1:4])
print(str[:4])
print('------------')
path = 'C:\nba\ticked.txt'
print(path)
path = r'C:\nba\ticked.txt'
print(path)
path = 'C:\\nba\\ticked.txt'
print(path)