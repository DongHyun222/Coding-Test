import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
visited = [[0]*m for _ in range(n)]
stx, sty = 0,0
q = deque([])

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            q.append([i,j])
            stx, sty = i,j
            break

dx,dy = [0,-1,0,1], [-1,0,1,0]

while q:
    x,y = q.popleft()

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
visited[stx][sty] = 0

for i in range(n):
    for j in range(m):
        print(visited[i][j],end=' ')
    print("")
