#백준 class3 1697번 
#숨바꼭질 N->K까지 BFS로 탐색
from collections import deque

N,K = map(int,input().split())
visited = [0] * 100001
#visited[N], visited[K] = 1,1

def in_range(num):
    if num >= 0 and num <= 100000:
        return True
    return False

def bfs():
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        for nx in (x-1,x+1,x*2):
            if in_range(nx) and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)
    
bfs() 