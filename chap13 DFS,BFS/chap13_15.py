#기출문제
#BFS 15번 
#백준 18352번

from collections import deque

N,M,K,X = map(int,input().split())          #N도시개수, M도로개수, K거리정보, X도시번호
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q:                                    #BFS(너비 우선 탐색) 수행 
    now = q.popleft()
    for next_node in graph[now]:            #이동 가능한 도시 다 확인 후 최단거리 갱신
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1,N+1):                      #최단거리K도시 오름차순 출력
    if distance[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)
