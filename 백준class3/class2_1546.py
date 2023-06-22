#백준 class2 1546번 문제
#새로 나와서 그냥 풀어봄 
#단순 계산식

N = int(input())
lst = list(map(int,input().split()))
max_score = max(lst)

cnt = 0
for score in lst:
    cnt += (score/max_score)*100
print(cnt/len(lst))
