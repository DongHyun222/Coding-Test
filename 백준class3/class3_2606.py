#백준 class3 2606번
# BFS를 활용해서 연결되어있는 컴퓨터수 찾기문제 
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = [0] * (N+1)
visited[1] = 1

cnt = 0
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(sum(visited)-1)
