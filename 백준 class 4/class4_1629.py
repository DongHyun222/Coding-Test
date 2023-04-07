#분할정복 이용해서 문제해결
#2^32 = 2^16 * 2^16 활용

import sys
input = sys.stdin.readline

#A를 B번 곱한 수를 C로 나눈 나머지 출력
A,B,C = map(int,input().split())

# ans = (A**B)%C
def solution(a,b,c):
    if b == 1:
        return a%c
    elif b % 2 == 0:
        return (solution(a,b//2,c)**2) % c
    else:
        return (solution(a,b//2,c)**2*a)%c

print(solution(A,B,C))

