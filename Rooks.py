"""
Задание с отбора в ШАД.
Сколько не занятых и неатакованных полей останется после того как на доску поставят n ладей.
"""

f = open('input.txt', 'r')
fc = f.read().split('\n')
f.close()

mn = fc[0].split()
n = int(mn[0])
m = int(mn[1])
hor = [0] * n
ver = [0] * n
allT = n*n
ch = cv = bannedT = 0
for i in range(1, len(fc)):
	t = list(fc[i].split())
	if hor[int(t[0]) - 1] == 1 and ver[int(t[1]) - 1] == 1:
		continue
	elif hor[int(t[0]) - 1] == 1:
		bannedT+=n-(i-1-ch)
		ch+=1
		ver[int(t[1]) - 1] = 1
		continue
	elif ver[int(t[1]) - 1] == 1:
		bannedT+=n-(i-1-cv)
		cv+=1
		hor[int(t[0])-1] = 1
		continue
	# bannedT+=2*n-2*(i-сh-1)-1
	bannedT+=n-(i-ch-1) + n-(i-cv-1) - 1
	hor[int(t[0]) - 1] = 1
	ver[int(t[1]) - 1] = 1
	
f = open('output.txt', 'w')
f.write(str(allT - bannedT))
f.close()
		