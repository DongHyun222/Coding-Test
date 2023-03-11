#인접한 식량 창고 약탈 X
N = int(input())
lst = list(map(int,input().split()))

dp = [0] * (N+1)
dp[0] = lst[0]
dp[1] = max(dp[0],lst[1])
# dp[2] = max(dp[1],dp[0]+lst[2])
# dp[3] = max(dp[2],dp[1]+lst[3])

for i in range(2,N):
    dp[i] = max(dp[i-1],dp[i-2]+lst[i])

print(dp[N-1])

