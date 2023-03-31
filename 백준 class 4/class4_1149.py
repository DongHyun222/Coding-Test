import sys
input = sys.stdin.readline

N = int(input())    #N번집의 색은 N-1,N+1번 집 색과 달라야함

rgb = []

for _ in range(N):
    rgb.append(list(map(int,input().split())))
    #빨,초,파

dp = [[1e9]*N for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = rgb[0][0], rgb[0][1], rgb[0][2]

for i in range(1,N):
    for j in range(3):
        if j == 0:
            dp[i][j] = rgb[i][j] + min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = rgb[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])
        else:
            dp[i][j] = rgb[i][j] + min(dp[i-1][j-2], dp[i-1][j-1])

# print(dp)
print(min(dp[N-1]))
