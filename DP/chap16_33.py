#백준 14501번(삼성문제)
#dp를 이용하되 뒤에서부터 채우는 방식

import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
time = []
price = []
max_value = 0

for _ in range(N):
    t,p = map(int,input().split())
    time.append(t)
    price.append(p)

for i in range(N-1,-1,-1):  
    t = time[i] +i  #남은기간+현재일자

    if t <= N:
        dp[i] = max(price[i] + dp[t], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max(dp))
