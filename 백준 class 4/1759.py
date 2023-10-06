#백준 1759
#백트래킹 이용해서 문제 해결
#처음에 접근들 잘못해서 코드가 드러워 졌는데 그냥 리스트에서 모음리스트 따로 안만들고
#아래처럼 조건확인하고 카운트 해줘도 런타임 안남

import sys
input = sys.stdin.readline

L,C = map(int,input().split())
lst = input().split()
lst.sort()
sub_lst = ['a', 'e', 'i', 'o', 'u']
# print(lst)
    
ans = []

def sol(cnt, sub_ans):
    if len(sub_ans) == L:
        mo_cnt = 0     #모음카운트
        for ch in sub_ans:
            if ch in sub_lst:
                mo_cnt += 1
        
        if mo_cnt >= 1 and L - mo_cnt >= 2:
            ans.append(''.join(sub_ans))
            return
    
    if cnt >= C:
        return
    
    sub_ans.append(lst[cnt])
    sol(cnt + 1, sub_ans)
    sub_ans.pop()
    sol(cnt + 1, sub_ans)


sol(0,[])
for a in ans:
    print(a)

