# 完数

def Prog6(n):
  count = 0
  res = []
  for i in range(1, n + 1):
    sum = 0
    for j in range(1, int(i / 2) + 1):
      if((i % j) == 0):
        sum += j
        if(sum == i):
          res.append(i)
  return ','.join(map(str, res))

print(Prog6(1000))
