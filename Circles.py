"""
Задано n треугольников, длины сторон которых являются целыми числами. 
Найдите наибольшее количество треугольников, имеющих один и тот же радиус вписанной окружности.
"""

f = open('input.txt', 'r')
fc = f.read().split('\n')
f.close()

q = int(fc[0])
r = [0] * (len(fc) - 1)

idx = 0
for i in range(1, len(fc)):
    Per = 0
    sides = list(fc[i].split())
    for j in sides: Per += int(j)
    p = Per / 2
    r[idx] = ((p - int(sides[0]))*(p - int(sides[1]))*(p - int(sides[2])))**(.5)
    idx+=1

maxQ = 0
for elem in r:
    cnt = 0
    for com_elem in r:
      if (elem == com_elem): cnt+=1
    maxQ = max(cnt, maxQ)

f = open('output.txt', 'w')
f.write(str(maxQ))
f.close()

