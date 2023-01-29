#백준 class3 9461번
#간단한 파도반 수열문제
#DP이용

T = int(input())

for _ in range(T):
    N = int(input())

    lst = [1,1,1,2,2,3]
    if N < 6:
        print(lst[N-1])
    else:
        for i in range(6,N):
            cnt = lst[-1] + lst[i-5]
            lst.append(cnt)
        print(lst[N-1])

