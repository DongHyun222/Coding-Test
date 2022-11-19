#PCCP시험대비 DFS예제
#소모 피로도가 최대로

answer = 1
def solution(k, dungeons):
    visited = [0] * len(dungeons)       #방문 기록
    global answer

    DFS(k,0,dungeons,visited)           #완전탐색하여 최대값 구하기
    return answer

def DFS(x,cnt,dungeons,visited):
    global answer
    answer = max(cnt,answer)

    for i in range(len(dungeons)):
        if visited[i] == 0 and dungeons[i][0] <= x:     #방문 안했고 최소피로도보다 피로도가 많이 남았을때
            visited[i] = 1
            DFS(x-dungeons[i][1], cnt + 1,dungeons, visited)
            visited[i] = 0

print(solution(80,[[80,20],[50,40],[30,10]]))


