#백준 class3 2667번 

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

visited = [[0]*N for _ in range(N)]

def in_range(a,b):
    if 0<= a < N and 0<= b <N:
        return True
    else:
        return False

def dfs(x,y):
    global N, cnt
    visited[x][y] = 1
    dxs,dys = [-1,0,1,0], [0,-1,0,1]
    
    for i in range(4):
        dx,dy = x+dxs[i], y+dys[i]
        if in_range(dx,dy):
            if graph[dx][dy] == 1 and visited[dx][dy] == 0:
                #visited[dx][dy] = 1
                cnt += 1
                dfs(dx,dy)
    return cnt

result = []
cnt = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            ans = dfs(i,j)
            result.append(ans)
            cnt = 1

if len(result) == 0:
    print(0)
else:
    print(len(result))
    result.sort()
    for re in result:
        print(re)
