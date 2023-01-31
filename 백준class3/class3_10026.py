#백준 class3 10026번
#재귀 문제 풀땐 sys.setrecursionlimit필수라더라
#보통 기본 재귀 깊이 제한이 1000밖에 안되서 안쓰고 제출하면 런타임에러남
#나머지는 그냥 DFS재귀로 풀면 됨

import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = []
visited = [[0]*N for _ in range(N)]
sec_visited = [[0]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(input()))

cnt1,cnt2 = 0,0

def in_range(a,b):
    global N
    return 0<=a<N and 0<=b<N

def DFS(x,y,lst):
    global cnt1,cnt2
    lst[x][y] = 1
    dxs,dys = [-1,0,1,0], [0,-1,0,1]
    index = graph[x][y]

    for i in range(4):
        nx,ny = x+dxs[i], y+dys[i]
        if in_range(nx,ny) and index == graph[nx][ny] and lst[nx][ny] == 0:
            DFS(nx,ny,lst)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt1 += 1
            DFS(i,j,visited)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if sec_visited[i][j] == 0:
            cnt2 += 1
            DFS(i,j,sec_visited)

print(cnt1, cnt2)
