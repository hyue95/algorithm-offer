# 最大公约数，最小公倍数
def Prog6(m, n):
  if(m < n):  # 保证 m > n
    temp = n
    n = m
    m = temp
  a = m
  b = n
  while(b != 0):
    temp = a % b
    a = b
    b = temp
  yshu = a
  bshu = m * n / a
  print(str(m) + '和' + str(n) + '的最大公约数为' + str(yshu))
  print(str(m) + '和' + str(n) + '的最小公倍数为' + str(bshu))

Prog6(9, 12)

