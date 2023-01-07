#백준 class3 7576번
#2차배열 BFS문제 

from collections import deque

M,N = map(int,input().split())
graph = []
q = deque()

for _ in range(N):
    graph.append(list(map(int,input().split())))

flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j])
            flag = True
ans = 0

dxs,dys = [1,-1,0,0], [0,0,1,-1]
def in_range(a,b):
    if 0<=a<N and 0<=b<M:
        return True
    else:
        return False

while q:
    x,y = q.popleft()
    cnt = 0
    for i in range(4):
        nx,ny = x+dxs[i], y+dys[i]
        if in_range(nx,ny) and graph[nx][ny] == 0:
            graph[nx][ny] = 1+graph[x][y]
            q.append((nx,ny))

for i in graph:
    for j in i:
        if j == 0:
            flag = False
    ans = max(ans,max(i))
if flag != False:
    print(ans-1)
else:
    print(-1)