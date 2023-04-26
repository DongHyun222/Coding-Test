#38번 플로이드워셜문제
#학생 성적을 확인할 수 있는 만큼 학생수 출력

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[1e9]*(N+1) for _ in range(N+1)]

for a in range(N+1):
    graph[a][a] = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            cnt += 1
    if cnt == N:
        ans += 1
    
print(ans)

