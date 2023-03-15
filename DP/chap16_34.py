import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.reverse()
dp = [1]*N

#DP[i]번째를 포함한 최대 길이
for i in range(1,N):
    for j in range(0,i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j]+1,dp[i])

print(N-max(dp))
