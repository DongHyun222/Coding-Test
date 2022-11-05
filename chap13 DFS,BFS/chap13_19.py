#기출문제
#BFS 19번 
#백준 14888번 삼성SW역량테스트

N = int(input())
lst = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())              #덧셈,뺄셈,곱셈,나눗셈

result_max = -999999999999
result_min = 99999999999

def dfs(i,now):
    global result_max, result_min, add, sub, mul, div

    if i == N:
        result_max = max(result_max,now)
        result_min = min(result_min,now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+lst[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-lst[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now*lst[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,int(now/lst[i]))
            div += 1

dfs(1,lst[0])
print(result_max)
print(result_min)

