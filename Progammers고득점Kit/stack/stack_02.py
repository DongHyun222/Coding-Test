#Programmers고득점 Kit Stack 2번문제
#deque안써도 해결가능한데 그냥 씀

from collections import deque

def solution(s):
    answer = True
    
    q = deque([])
    
    if s[0] != '(':
        return False
    q.append(s[0])
    
    for i in range(1,len(s)):
        if s[i] == '(':
            q.append(s[i])
        else:
            if len(q) == 0:
                return False
            elif q[-1] != '(':
                return False
            else:
                q.pop()

    if len(q) != 0:
        return False

    return True