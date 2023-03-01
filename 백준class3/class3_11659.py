#백준 11659번
#구간합 구하는 문제인데 그냥 더하면 시간오류남
#누적합을 이용해서 해결해야댐

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0] * 100001

for i in range(1,N+1):
    dp[i] = dp[i-1] + lst[i-1]

for _ in range(M):
    i,j = map(int,input().split())
    print(dp[j] - dp[i-1])
    
