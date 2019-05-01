from collections import deque

dist = [None] * 8

#Save graf as adjacency matrix
graf = [[1,5],[0,2,3,5],[1,3],[2,1],[7,6],[0,1,6],[5,4,7],[4,6]]

def BFS(start):
 global  dist, graf
 a = deque()
 a.append(start)
 dist[start] = 0
 while a:
     #Here I should set another counter because currentDist var doesnt work
     #correctly
     elem = a.pop()
     for i in graf[elem]:
         if dist[i] == None:
           dist[i] = dist[elem]+1
           a.append(i)

BFS(0)
print (dist)