import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

def dfs(start):
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
cnt = 0

for i in range(1,N+1):
    if visited[i] == 0:
        if len(graph[i]) == 0:
            cnt += 1
            visited[i] = 1
        else:
            dfs(i)
            cnt += 1

print(cnt)