#편집거리문제
#2차원 배열에 편집값 넣어서 최소편집거리 찾기

#삽입,삭제,교체 3개
A = input()
B = input()

N = len(A)
M = len(B)

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][0] = i
for i in range(1,M+1):
    dp[0][i] = i

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

print(dp[N][M])

