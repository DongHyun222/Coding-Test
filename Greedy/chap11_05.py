#그리디 5번문제
#2중for문으로 간단한문제

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0

for i in range(len(lst)):
    for j in range(i,len(lst)):
        if lst[i] != lst[j]:
            cnt += 1

print(cnt)
