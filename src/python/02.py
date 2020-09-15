import math

def Prog2(m, n):
  count = 0
  for item in range(m, n + 1):
    if(isPrime(item)):
      count += 1
  return count

def isPrime(n):
  flag = False
  if(n == 1):
    flag = False
  else:
    for i in range(2, int(math.sqrt(n)) + 1):
      if((n % i) == 0):
        flag = False
        break
      else:
        flag = True
  return flag

print(Prog2(100, 200))
