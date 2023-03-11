#화폐 N개 -> M원 가치가 될때 화폐개수
N,M = map(int,input().split())
lst = []

for _ in range(N):
    lst.append(int(input()))

dp = [10001]*(M+1)  #화폐개수 저장
dp[0] = 0

for i in range(N):
    for j in range(lst[i],M+1):
        dp[j] = min(dp[j], dp[j-lst[i]]+1)
    #print(dp)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
