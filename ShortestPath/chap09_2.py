#백준 실전문제 2번
#플로이드 워셜 알고리즘 문제

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[1e9]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    graph[a][b] = 1
    graph[b][a] = 1
    
X,K = map(int,input().split())
X,K = X-1,K-1

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#print(graph)
result = graph[0][K] + graph[K][X]
if result >= 1e9:
    print("-1")
else:
    print(result)
