import sys
import heapq

input = sys.stdin.readline

#도시 C로 보낼수 있는 도시개수 및 총시간 출력
N,M,C = map(int,input().split()) 
graph = [[] for i in range(N+1)]
distance = [1e9] * (N+1)

for _ in range(M):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def answer(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:    #distance에 저장된 경로가 최단경로일때 
            continue
        for i in graph[now]:
            cost = dist + i[1]  #1번째가 걸리는 시간
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

answer(C)

cnt = 0
max_distance = 0

for d in distance:
    if d != 1e9:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)

