from collections import deque

N,M = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(grpah,start):
    num = [0]*(N+1)
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a] + 1
                visited[i] = 1
                q.append(i)
    return sum(num)

cnt = 99999999999
result = 0

for i in range(1,N+1):
    visited = [0 for _ in range(N+1)]
    x = bfs(graph,i)
    if cnt > x:
        cnt = x
        result = i
print(result)
