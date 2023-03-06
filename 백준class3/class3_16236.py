from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
#0은 빈칸, 1,2,3,4,5,6은 물고기 크기, 9는 아기상어 위치
#아기상어 처음 크기는 2, 크기만큼 물고기 먹으면 += 1
#2보다 작으면 먹을수 있음, 2이면 그냥 통과, 2보다 크면 못지나감
graph = []
a,b = 0,0
q = deque()
for i in range(N):
    x = list(map(int,input().split()))
    graph.append(x)
    if 9 in x:
        a,b = i,x.index(9)

def in_range(aa,bb):
    return 0<=aa<N and 0<=bb<N

size = 2
dx,dy = [-1,0,1,0], [0,-1,0,1]
def can_eat(a,b,shark_size):    #먹을수 있는 물고기 찾기
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    temp = []
    q.append((a,b))
    while q:
        x,y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if in_range(nx,ny) and visited[nx][ny] ==0:
                if graph[nx][ny] <= shark_size: #작을때
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
    #가까운 물고기가 많으면 위,왼쪽 순으로 
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0     #물고기 먹은 갯수
result = 0
while True:
    shark = can_eat(a,b,size)
    if len(shark) == 0:
        break
    
    nx,ny,dist = shark.pop()
    result += dist

    graph[a][b],graph[nx][ny] = 0,0
    a,b = nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0


print(result)

