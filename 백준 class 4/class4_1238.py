#백준 1238 다익스트라 문제
#일반 다익스트라와 다르가 왔다갔다 최소거리를 생각해야되서 마지막에 
#for문에 ans함수 돌려서 매지점마다 결과 확인해야됨

import sys
import heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())    #N명 M개의 간선, X로 감
graph = [[] for _ in range(N+1)]

for _ in range(M):
    #a->b로 t만큼 걸린다
    a,b,t = map(int,input().split())
    graph[a].append((b,t))

def ans(start):
    q = []
    distance = [1e9]*(N+1)

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

ans(X)

result = 0
for i in range(1,N+1):
    lst1 = ans(i)   #출발지점->도착지점 최소거리
    lst2 = ans(X)   #도착지점->출발지점 최소거리
    result = max(result,lst1[X] + lst2[i])
print(result)
