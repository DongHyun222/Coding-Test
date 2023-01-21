import collections
T = int(input())
asd = collections.defaultdict()
for _ in range(T):
    N = int(input())
    cloth = {}

    for i in range(N):
        lst = list(input().split())
        if lst[1] in cloth:
            cloth[lst[1]].append(lst[0])
        else:
            cloth[lst[1]] = [lst[0]]

    cnt = 1
    for wear in cloth:
        cnt *= (len(cloth[wear]) + 1)
    print(cnt-1)


''' 카운터 이용한 예시
from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)'''