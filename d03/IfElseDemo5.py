#測試
def x():
   print('x()')
   return True
def y():
    print( 'y()')
    return False
def z():
    print('z()')
    return False
if x() or y() and z():
    print("Yes")
else:
    print("no")

if y() and x() or x():
    print("Yes")
else:
    print("no")

if y() or y() and z():
    print("Yes")
else:
    print("no")

