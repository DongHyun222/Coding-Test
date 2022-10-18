#기출문제
#구현 11번문제
#삼성전자 SW역량 테스트
#ㄹㅇ 여러번 다시 풀어봐야될 문제 겁나어려움

N = int(input())
K = int(input())
data = [[0]*(N+1) for _ in range(N+1)]
info = []

for _ in range(K):
    a,b = map(int,input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def simulate():
    x,y = 1,1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= N and 1 <= ny and ny <= N and data[nx][ny] != 2:
            if data[nx][ny] ==0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))

        else:
            time += 1
            break
        x,y = nx,ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index += 1
    return time

print(simulate())

