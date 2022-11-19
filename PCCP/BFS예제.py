#PCCP시험대비 BFS예제
#송아지 찾기

from collections import deque
def solution(s,e):          #s는 사람위치, e는 송아지 위치
    answer = 0
    q = deque([s])
    goes = [-1,1,5]
    visited = [0] * 10000
    visited[s] = 1

    while q:
        lenth = len(q)
        for i in range(lenth):
            x = q.popleft()
            for go in goes:
                xx = x+go
                if xx == e:         #송아지 찾았을 경우 점프횟수 리턴
                    return (answer + 1)
                if xx > 0 and xx < 10001 and visited[xx] ==0:
                    visited[xx] = 1
                    q.append(xx)
        answer += 1
    
    return answer

print(solution(5,14))