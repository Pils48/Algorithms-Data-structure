"""
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately 
following ranking number.
"""

def climbingLeaderboard(scores, alice):
    #Удаление повторяющихся элементов в массиве
    toDelete = list()
    for i in range(len(scores) - 1): #Из-за добавления +1 к индексу не бежим до len(scores)
        if scores[i] == scores[i+1] : toDelete.append(scores[i])
    for a in toDelete:
        scores.remove(a)

    #Бинарный поиск промежутка куда необходимо вставить элемент
    for i in range(len(alice)):
        tail = 0
        head = len(scores) - 1
        while (head - tail)//2 != 0:
            mid = tail + (head - tail)//2
            if (scores[mid] > alice[i]) : tail = mid
            elif (scores[mid] < alice[i]) : head = mid
            else:
                alice[i] = mid + 1
                break
        else: #Поиск места элемента из 4-х возможных позиций
            if scores[tail] < alice[i] : alice[i] = tail + 1 # + 1 переход от индекса к месту
            elif scores[tail] > alice[i] and scores[head] < alice[i] : alice[i] = tail + 1 + 1
            elif scores[head] > alice[i] : alice[i] = head + 1 + 1
            elif scores[tail] == alice[i] : alice[i] = tail + 1
            elif scores[head] == alice[i] : alice[i] = head + 1
    return alice

scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
climbingLeaderboard(scores, alice)