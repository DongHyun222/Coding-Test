#기출문제
#DFS 16번 삼성전자 SW테스트
#백준 14502번

N,M = map(int,input().split())
graph = []
visited = [[0]*M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 바이러스가 상하좌우로 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >=0 and ny < M:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 2
                virus(nx,ny)

# 안전영역 크기 계산
def get_answer():
    score = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                score += 1  
    return score

#dfs를 이용해서 울타리 설치하고 매번 안전영역 크기계산
def dfs(count):
    global result
    #울타리 3개일때
    if count == 3:
        for i in range(N):
            for j in range(M):
                visited[i][j] = graph[i][j]
    #각 바이러스 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 2:
                    virus(i,j)
        result = max(result, get_answer())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
dfs(0)
print(result)
