#기출문제
#정렬 23번
# 국영수문제

N = int(input())
lst = []

for _ in range(N):
    lst.append(input().split())

lst.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in lst:
    print(student[0])

