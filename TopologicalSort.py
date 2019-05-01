WHITE = 0
GREY = 1
BLACK = 2
color = [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE]
orderNumber = len(color)
graf = [[1],[],[1],[2],[3],[2]]
def DFS(i):
    global orderNumber, color
    color[i] = GREY
    for j in graf[i]:
        if color[j] == WHITE:
             DFS(j)
    #color[i] == BLACK
    color[i] = orderNumber
    orderNumber -= 1
DFS(0)
def findingConnectionComponents():
   for i in range(len(color)):
      if color[i] == 0:
         DFS(i)
findingConnectionComponents()
print(color)

