N,M = map(int,input().split())
graph = []
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))

max_result = 0

def in_range(a,b):
    return (0 <= a < N and 0 <= b < M)

def find1(a,b,cnt,result):
    global max_result
    if cnt == 4:
        max_result = max(result,max_result)
        return
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx,ny = a+dx[i], b+dy[i]
        if in_range(nx,ny) and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            find1(nx,ny,cnt+1,result+graph[nx][ny])
            visited[nx][ny] = 0

def find2(a,b,result):
    global max_result
    dx,dy = [-1,0,1,0], [0,-1,0,1]
    for i in range(4):
        tmp = result
        for j in range(3):
            nn = (j+i)%4
            nx,ny = a+dx[nn],b+dy[nn]
            if in_range(nx,ny):
                tmp += graph[nx][ny]

        max_result = max(tmp,max_result)

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        find1(i,j,1,graph[i][j])
        visited[i][j] = 0

        find2(i,j,graph[i][j])

print(max_result)

