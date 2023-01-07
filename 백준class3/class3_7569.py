#백준 class3 7569번
#3차원배열
#결국 배열 구현만 잘하고 BFS로 마무리하면됨
from collections import deque

M,N,H = map(int,input().split())
#M,N은 상자 크기  H는 상자수(높이)
graph = []
q = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,input().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

dxs = [-1,1,0,0,0,0]
dys = [0,0,-1,1,0,0]
dzs = [0,0,0,0,-1,1]

while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx = x+dxs[i]
        ny = y+dys[i]
        nz = z+dzs[i]
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = 1+graph[x][y][z]
            q.append([nx,ny,nz])

ans = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                print(-1)
                exit(0)
            ans = max(ans,graph[z][y][x])
print(ans-1)
