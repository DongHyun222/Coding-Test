#백준 class3 1764번 
#중복없이 이름 정렬해서 출력

import sys
N,M = map(int,sys.stdin.readline().split())  

N_set = set()
M_set = set()

for _ in range(N):
    N_set.add(input())

for _ in range(M):
    M_set.add(input())

ans = sorted(list(N_set & M_set))

print(len(ans))
for name in ans:
    print(name)