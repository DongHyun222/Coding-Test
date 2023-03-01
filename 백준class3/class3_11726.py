#백준 11726번
#2xN 크기의 직사각형 1x2,2x1타일로 채우기, 간단함

import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * (N+1)
if N <= 2:
    print(N)
else:
    lst[2] = 2
    lst[3] = 3
    if N >= 3:
        for i in range(4,N+1):
            lst[i] = lst[i-1] + lst[i-2]
        print(lst[N]%10007)    
    else:
        print(lst[N]%10007)

