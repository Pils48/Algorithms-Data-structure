"""
Помогите Мише с помощью компьютера решить поставленную задачу.
Напишите программу, которая по заданным значениям n и k вычисляет последнюю ненулевую цифру
суммы k-х степеней факториалов всех целых чисел в промежутке от 0 до n.
"""

def f(i):
  if i == 1 or i == 0:
    return 1
  else:
    return i * f(i - 1)

def findLast(s):
   r = 0
   i = 1
   while r == 0:
      r = s%10**i
      i+=1
   return r//10**(i-2)

inp = list(input().split())
n = int(inp[0])
k = int(inp[1])
s = res = 0
if (n >= 4 and k != 0):
    for i in range(5): s += f(i) ** k
    res = findLast(s)
elif (n < 4 and n != 0 and k != 0):
    for i in range(n + 1): s += f(i) ** k
    res = findLast(s)
elif (k == 0):
    res = findLast(n+1)
elif (n == 0):
    res = 1
print(res)