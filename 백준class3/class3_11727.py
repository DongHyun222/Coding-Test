import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * (N+1)
if N == 1:
    print(N)
elif N == 2:
    print(3)
else:
    lst[2] = 3
    lst[3] = 5
    for i in range(4,N+1):
        lst[i] = lst[i-1] + lst[i-2] * 2
    print(lst[N]%10007)


