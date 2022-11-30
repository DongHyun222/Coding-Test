#백준 class3 2579번 
#계단 오르기 문제 
#조건이 너무 더럽다(런타임에러 이상하게난다)

N = int(input())
stairs = [0] * 302
for i in range(1,N+1):
    stairs[i] = int(input)

ans = [0] * 302     #계단 1,2,3초기화
ans[1] = stairs[1]
ans[2] = stairs[1]+stairs[2]
ans[3] = max(stairs[1] + stairs[3],stairs[2]+stairs[3])

for i in range(4,N+1):  #계단 4부터 조건에 맞게 최대값
    ans[i] = max(ans[i-3]+stairs[i-1] + stairs[i], ans[i-2]+stairs[i])

print(ans[N])
