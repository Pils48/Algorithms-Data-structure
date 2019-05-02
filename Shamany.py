"""
Таким образом, каждое заклинание Ti, начиная с i = 2, состояло из последовательного исполнения заклинаний Ti - 2 и Ti - 1. При последовательном исполнении заклинаний между ними делалась небольшая пауза, 
так что новые слова при конкатенации образовываться не могли.
В разных случаях использовались разные заклинания: например, для проведения обряда инициации шаман должен был произнести заклинание так, 
чтобы имя духа S, встречавшееся как минимум в одной из ключевых фраз, было произнесено ровно K раз.
Антропологи обратились к вам с просьбой: зная начальные ключевые фразы A и B, имя духа S, 
встречающееся в одной или обеих из них, а также число K, определить число N — наименьший номер заклинания TN, в котором слово S встречается ровно K раз.
"""
def contain(s = str, c = str):
    sep = ""
    idx = 0
    while ord(s[idx]) > 32 and ord(s[idx]) < 127 and idx < len(s) - 1:
        idx+=1
    else: sep = s[idx]
    cnt = 0
    s = s.lower()
    c = c.lower()
    words = list(s.split(sep))
    for word in words:
        if (word == c):
            cnt+=1
    return cnt



def write_to_file(c):
    f = open('output.txt', 'w')
    f.write(c)
    f.close()

f = open('input.txt', 'r')
fc = f.read().split("\n")
f.close()

res = ""
a = b = q = 0
a+=contain(fc[0], fc[2])
b+=contain(fc[1], fc[2])

pr2 = a
pr1 = b
it = 1
while q < int(fc[3]):
    it+=1
    q = pr2 + pr1
    pr2 = pr1
    pr1 = q
if q == int(fc[3]):
    res = str(it)
    write_to_file(res)
else:
    res = "Impossible"
    write_to_file(res)
