
def Prog1( n):
  if n == 1 or n == 2:
    return n
  else:
    return Prog1( n - 1) + Prog1( n - 2)

print(Prog1(3))
