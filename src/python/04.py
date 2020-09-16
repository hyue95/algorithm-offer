
def Prog4(num):
  s = str(num) + ' = '
  for i in range(2, num + 1):
    while(num % i == 0 and num != i):
      num /= i
      s += str(i) + ' * '
    if(num == i):
      s += str(i)
      break
  return s

print(Prog4(90))

