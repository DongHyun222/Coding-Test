#백준 11286번
#절대값 힙으로 11279와 비슷

import heapq
import sys

lst = []
N = int(input())
input = sys.stdin.readline

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst)[1])
    else:
        heapq.heappush(lst,(abs(x),x))
        
