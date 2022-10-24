#기출문제
#BFS 17번
#백준 18405번

from collections import deque

N,K = map(int,input().split())              #N은 시험관 크기, K는 바이러스수
graph = []
data = []

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))        #data 바이러스 종류, 0초, (i,j)좌표

S,X,Y = map(int,input().split())            # S는 시간, X,Y는 좌표

dx,dy = [-1,1,0,0], [0,0,-1,1]

data.sort()
q = deque(data)

# BFS탐색
while q:
    virus,s,x,y = q.popleft()
    if s == S:
        break
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
                

print(graph[X-1][Y-1])
