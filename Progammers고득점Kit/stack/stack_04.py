#Programmers고득점 Kit Stack 4번문제
#문제설명대로 규칙따라가면 쉽게 해결함
#visited대신 dic써도 문제해결할수 있을듯

from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque(priorities)
    visited = deque([i for i in range(len(q))])
    cnt = 0
    # print(visited)
    
    while q:
        now = q.popleft()
        now_v = visited.popleft()
        if len(q) != 0 and now < max(q):
            q.append(now)
            visited.append(now_v)
        else:
            cnt += 1
            if now_v == location:
                return cnt

    
    return answer