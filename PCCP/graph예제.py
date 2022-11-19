#PCCP시험대비 graph예제
#트리형태 전선을 2개로 분할하여 최소차이찾기

cnt = 0
def solution(n,wires):
    global cnt
    answer = 99999999999       #최소값 찾기위해 큰값 미리 설정
    graph = [[] for _ in range(n+1)]

    for a,b in wires:           #연결되있는 전선 그래프에 저장
        graph[a].append(b)
        graph[b].append(a)

    for x,y in wires:
        cnt = 0
        visited = [0] * (n+1)
        visited[y] = 1
        DFS(x,visited,graph)        #모든 그래프 탐색

        result = abs(cnt-(n-cnt))
        answer = min(result,answer)

    return answer

def DFS(x,visited,graph): 
    global cnt
    visited[x] = 1
    cnt +=1
    for i in graph[x]:
        if visited[i] == 0:
            DFS(i,visited,graph)

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))