#Programmers고득점 Kit Stack 3번문제
#lst에 넣어주는 값만 잘 생각하면 쉽게 해결

import math

def solution(progresses, speeds):
    answer = []
    lst = []
    
    for i in range(len(speeds)):
        lst.append(math.ceil((100-progresses[i])/speeds[i]))
    
    lst_max = lst[0]
    cnt = 1
    
    for i in range(1,len(lst)):
        if lst[i] > lst_max:
            lst_max = lst[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer