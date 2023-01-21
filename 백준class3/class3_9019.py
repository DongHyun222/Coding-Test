from collections import deque
T = int(input())

def dd(x):
    x = x*2
    if x > 9999:
        x = x%10000
    return x

def ss(x):
    x -= 1
    if x == -1:
        x = 9999
    return x

def ll(x):
    front = x % 1000
    back = x // 1000
    x = front * 10 + back
    return x

def rr(x):
    front = x % 10
    back = x // 10
    x = front*1000+back
    return x

def bfs(a,b,visited):
    q = deque()
    q.append((a,"")) 
    visited[a] = 1
    while q:
        X,ans = q.popleft()
        if X == b:
            print(ans)
            return
        
        tmp = dd(X)
        if visited[tmp] == 0:
            visited[tmp] = 1
            q.append((tmp,ans+"D"))
        
        tmp = ss(X)
        if visited[tmp] == 0:
            visited[tmp] = 1
            q.append((tmp,ans+"S"))

        tmp = ll(X)
        if visited[tmp] == 0:
            visited[tmp] = 1
            q.append((tmp,ans+"L"))
        
        tmp = rr(X)
        if visited[tmp] == 0:
            visited[tmp] = 1
            q.append((tmp,ans+"R"))

for _ in range(T):
    A,B = map(int,input().split())
    visited = [0] * 10000
    bfs(A,B,visited)
