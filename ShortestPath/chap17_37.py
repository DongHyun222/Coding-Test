import sys
input = sys.stdin.readline

N = int(input())    #도시 개수
M = int(input())    #버스 개수

graph = [[1e9]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int,input().split())    #a->b, c는 비용
    a,b = a-1,b-1
    graph[a][b] = min(graph[a][b],c)

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j] >= 1e9:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print("")

