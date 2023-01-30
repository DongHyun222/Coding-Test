#백준 11047번
#간단한 동전갯수찾기문제

N,K = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0
for i in range(N-1,-1,-1):
    while True:
        if lst[i] <= K:
            K -= lst[i]
            cnt += 1
        else:
            break
print(cnt)

