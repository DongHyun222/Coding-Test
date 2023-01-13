from collections import deque

n,l,r = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

def process(x,y,index):
    united = []     #연결된 연합나라담는 리스트
    united.append((x,y))
    
    q = deque()
    q.append((x,y))
    union[x][y] = index     #연결된 연합에 현재 번호 할당
    summary = graph[x][y]
    cnt = 1     #현재 연결된 연합 국가 수

    while q:    #bfs수행
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    cnt += 1
                    united.append((nx,ny))

    for i,j in united:
        graph[i][j] = summary // cnt
    return cnt

total_cnt = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   #해당 나라가 연합에 없다면
                process(i,j,index)
                index += 1      #연합 번호 구분해주기
    if index == n*n:
        break
    total_cnt += 1
    print(graph)
print(total_cnt)

