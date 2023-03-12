import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int,input().split())))
if N == 1:
    print(lst[0][0])
    exit(0)

dp = [[0]*i for i in range(1,N+1)]

dp[0][0] = lst[0][0]
dp[1][0] = dp[0][0] + lst[1][0]
dp[1][1] = dp[0][0] + lst[1][1]

if N == 2:
    print(max(dp[1]))
    exit(0)

for i in range(2,N):
    for j in range(len(lst[i])):
        if j == 0:
            dp[i][j] = lst[i][j] + dp[i-1][j]
        elif j == (len(lst[i])-1):
            # print("*****")
            dp[i][j] = lst[i][j] + dp[i-1][j-1]
        else:
            # print(i,j)
            dp[i][j] = lst[i][j] + max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[N-1]))

