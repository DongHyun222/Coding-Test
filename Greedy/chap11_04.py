#그리디 4번문제
#아래 cnt에 lst작은값들인 i를 더해보면서
#cnt가 i보다 작아질때 만들수 없는 금액이라서 break하는데 빡세네

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()

cnt = 1
for i in lst:
    if cnt < i:
        break
    cnt += i
    # print(cnt)

print(cnt)
