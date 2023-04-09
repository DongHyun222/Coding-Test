#이 문제 풀때 알아야할 아이디어
#그래프에서 서로 가장 멀리 떨어져있는 두 노드는
#임의의 한 노드에서 가장 떨어진 노드 중 하나이다.

import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]

#정점,거리 순으로 입력 마지막에 -1
for _ in range(V):
    vertex = list(map(int,input().split()))

    if len(vertex) == 2:    #간선이 없을때
        continue
    
    for i in range(1,len(vertex)-1,2):
        a,b = vertex[i], vertex[i+1]    #a로 가는데 b만큼 걸림
        graph[vertex[0]].append([a,b])

ans = 0
# print(graph)
visited = [0]*(V+1)
max_vertex = 0

def dfs(x,cnt):
    global ans, max_vertex
    visited[x] = 1

    if ans < cnt:
        ans = cnt
        max_vertex = x
    # ans = max(cnt,ans)

    for gg in graph[x]:
        if len(gg) != 0:
            a,b = gg[0], gg[1]      #a로 가는데 b만큼 걸림
            if visited[a] == 0:     #방문 안했으면
                cnt += b
                dfs(a,cnt)
                visited[a] = 0
                cnt -= b
    
    return ans

ans_1 = dfs(1,0)
visited = [0]*(V+1)
ans_2 = dfs(max_vertex,0)

print(max(ans_1,ans_2))
