#백준 11279번
#최대힙 문제
#원래 heapq는 최소힙이므로 아래처럼 튜플로 묶어서 최대힙으로 변경

import heapq
import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(lst) == 0:
            print(0)
        else:
            a = heapq.heappop(lst)[1]
            print(a)
    else:
        heapq.heappush(lst,(-x, x))     #(인덱스,값)으로 묶어서 최대힙으로

