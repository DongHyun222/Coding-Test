import sys
input = sys.stdin.readline

N = int(input())
lst = []
ans = []
cur = 1

for _ in range(N):
    num = int(input())
    while cur <= num:
        lst.append(cur)
        cur += 1
        ans.append('+')

    if lst[-1] == num:
        ans.append('-')
        lst.pop()
    else:
        print("NO")
        exit(0)

for i in ans:
    print(i)

