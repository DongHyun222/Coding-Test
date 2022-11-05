#백준 클래스3 1074번

N,r,c = map(int,input().split())
result = 0

while N != 0:           #4분면으로 계속 분할정복
    N -= 1
    n = 2**N

    #1사분면
    if r < n and c < n:
        continue
    #2사분면
    elif r < n and c >= n:
        result += n*n*1
        c -= n
    #3사분면
    elif r >= n and c < n:
        result += n*n*2
        r -= n
    elif r >= n and c >= n:
        result += n*n*3
        c -= n
        r -= n
print(result)
