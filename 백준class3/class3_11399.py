#백준 11399번
#이것도 간단한 정렬,그리디 문제

N = int(input())
lst = list(map(int,input().split()))

lst.sort()
cnt = 0
ans = 0
for i in lst:
    cnt += i
    ans += cnt
print(ans)
