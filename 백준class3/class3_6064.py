#백준 class3 6064번
#abn가 M의 배수임을 못알아내면 못품 

T = int(input())

for _ in range(T):
    M,N,x,y = map(int,input().split())
    ans = x

    while True:
        if ans > M*N:
            ans = -1
            break
        if (ans-x)%M == 0 and (ans-y)%N == 0:
            break
        ans += M

    print(ans)
