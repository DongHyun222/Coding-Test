from collections import deque

N,M,V = map(int,input().split())        #N은 정점수,M은간선수, V는 시작점
graph = [[0]*(N+1) for i in range(N+1)]

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited_dfs[v] = 1
    print(v,end=' ')
    
    for i in range(1,N+1):      #1~N까지 재귀로
        if(visited_dfs[i] == 0 and graph[v][i] == 1):
            visited_dfs[i] = 1
            dfs(i)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = 1

    while q:    #q가 빌때까지
        x = q.popleft()
        print(x,end=' ')
        for i in range(1,N+1):
            if(visited_bfs[i] == 0 and graph[x][i] == 1):
                q.append(i)
                visited_bfs[i] = 1
dfs(V)
print("")
bfs(V)