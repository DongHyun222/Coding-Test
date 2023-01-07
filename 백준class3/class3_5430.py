#백준 class3 5430번 
#입력케이스 너무 더러움
#R뒤집기, D버리기
from collections import deque
T = int(input())

for _ in range(T):
    p = list(str(input()))
    n = int(input())
    lst = input()[1:-1].split(',')
    lst = deque(lst)
    if n == 0:
        lst = deque()
    
    R = 0
    flag = 1
    for i in range(len(p)):
        if p[i] == 'R':
            R += 1
        elif p[i] == 'D':
            if len(lst) == 0:
                print('error')
                flag = 0
            else:
                if R % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()

    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('['+",".join(lst)+']')
        else:
            lst.reverse()
            print('['+",".join(lst)+']')

