import sys
import heapq
#1번에서 N번 정점으로 이동
input = sys.stdin.readline

N,E = map(int,input().split()) #N은 정점, E는 간선
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())    #a<->b 양방향 거리 c
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())
# 1-> v1-> v2 -> N번으로 가야됨 v1,v2순서상관 x

def ans(a,b):
    if a == b:
        return 0
    q = []
    heapq.heappush(q, (0,a))
    distance = [1e9] * (N+1)

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
    return distance[b]
                
result = min(ans(1,v1) + ans(v1,v2) + ans(v2,N), ans(1,v2) + ans(v1,v2)+ ans(v1,N))
if result < 1e9:
    print(result)
else:
    print("-1")
