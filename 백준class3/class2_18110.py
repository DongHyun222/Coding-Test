import sys
input = sys.stdin.readline

def my_round(num):
    if num-int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
    exit(0)
    
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

minus = my_round(n*0.15)
cnt = 0

for i in range(minus,n-minus):
    cnt += lst[i]

print(my_round(cnt/(n-(2*minus))))
