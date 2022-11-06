#기출문제
#정렬 24번

N = int(input())
lst = list(map(int,input().split()))
lst.sort()

mini = 999999999
result = 0

for i in range(lst[0], lst[-1]+1):
    cnt = 0
    for x in lst:
        cnt += abs(x-i)
    
    if cnt < mini:
        mini = cnt
        result = i
    
print(result)

