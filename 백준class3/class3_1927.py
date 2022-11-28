#백준 class3 1927번 
#최소 힙

import heapq
import sys
hQ = []

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(hQ) == 0:
            print(0)
        else:
            print(heapq.heappop(hQ))
    else:
        heapq.heappush(hQ,x)
