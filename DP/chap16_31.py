import sys
input = sys.stdin.readline
#첫번째열 금캐기시작
T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    graph = []

    for i in range(n):
        graph.append(lst[i*m:(i*m)+m])

    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] += graph[i][0]

    ans = 0
    for j in range(1,m):
        for i in range(n):
            for k in range(-1,2):
                x = i+k
                if 0<=x<n:
                    dp[i][j] = max(dp[i][j], dp[x][j-1]+graph[i][j])
                    ans = max(dp[i][j],ans)
    # print(graph)
    # print(dp)
    print(ans)


