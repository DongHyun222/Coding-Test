#기출문제
#구현 12번문제
#캬카오 2020공채

N = int(input())
K = int(input())

graph = [
    [0]*N for _ in range(N)
]

for _ in range(K):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1

L = int(input())

dxs,dys = [0,1,0,-1],[1,0,-1,0]

asd = 0
dx,dy = dxs[asd],dys[asd]

def change_root(a):
    global asd
    if a == "L":
        asd = (asd-1)%4
    else:
        asd = (asd+1)%4
    return asd

def in_range(q,w):
    if 0 <= q and q < N and 0 <= w and w < N:
        return True
    else:
        return False

x,y = 0,0
cnt = 0
graph[x][y] = 2
q = [(x,y)]

for _ in range(L):
    aa = True

    m,l = input().split()
    l = int(l)

    for i in range(l):
        nx,ny = x+dx, y+dy
        if in_range(nx,ny) and graph[nx][ny] != 2:
            cnt += 1
            graph[nx][ny] = 2
            q.append((nx,ny))
        else:
            aa = False
            break
    if aa == False:
        print(cnt)
        break

    zz = change_root(x)
    dx,dy = dxs[zz],dys[zz]


