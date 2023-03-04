#백준 class3 18870번 
#좌표압축문제
#좌표를 작은순서로 set,sort한다음에 dic에 순서대로 dic에 저장해서 출력

import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int,input().split()))
# lst_sort = sorted(lst)
set_lst = list(sorted(set(lst)))
dic = {}

for i in range(len(set_lst)):
    dic[set_lst[i]] = i

for i in lst:
    print(dic[i],end=' ')

