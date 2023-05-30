#Promgrammers 118667번
#카카오 2022
#두 큐합이 같은거 만들기

from collections import deque

def solution(queue1, queue2):
    answer = -1
    q1,q2 = deque(queue1), deque(queue2)
    
    sumq = (sum(q1) + sum(q2))
    sum_q1 = sum(q1)
    if sumq % 2 == 1:
        return -1
    else:
        sumq = sumq//2
    
    n = (len(q1) + len(q2))
    cnt = 0
    
    while q1 and q2:
        if sum_q1 > sumq:
            sum_q1 -= q1.popleft()
            cnt += 1
        elif sum_q1 < sumq:
            tmp = q2.popleft()
            q1.append(tmp)
            sum_q1 += tmp
            cnt += 1
        else:
            return cnt
    # for i in range(n):
    #     if sum(q1) == sumq:
    #         break
    #     if sum(q1) > sumq:
    #         q2.append(q1.popleft())
    #     else:
    #         q1.append(q2.popleft())
    #     cnt += 1
    # if cnt != n:
    #     return cnt
    
    return -1