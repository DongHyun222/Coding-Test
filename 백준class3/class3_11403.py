#백준 11403번
#경로찾는 문제로 dfs로 연결지점 찾아서 출력

import sys
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0]*N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    visited[x][y] = 1
    for a in range(N):
        if graph[y][a] == 1 and visited[x][a] == 0:
            dfs(x,a)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
for i in visited:
    print(*i)

