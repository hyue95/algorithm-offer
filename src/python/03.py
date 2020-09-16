
def Progs(m, n):
  s = ''
  for i in range(m, n + 1):
    if(isLotus(i)):
      s += str(i) + ' '
  return s    

def isLotus(num):
  a = int(num / 100)
  b = int((num - a * 100) / 10)
  c = num - a * 100 - b * 10
  sum = a * a * a + b * b * b + c * c * c
  if(num == sum):
    return True
  else:
    return False
  

print(Progs(100, 999))
