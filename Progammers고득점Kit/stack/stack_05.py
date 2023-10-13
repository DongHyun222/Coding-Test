#Programmers고득점 Kit Stack 5번문제
#문제설명이 제대로 안되어있음ㄹㅇ
#다리 하중에 무게를 추가해주는 방식으로 풀이

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    q = deque([0] * bridge_length)
    truck = deque(truck_weights)
    sec = 0
    cnt = 0
    
    while True:
        if len(truck) == 0:
            break
        
        sec += 1
        cnt -= q.popleft()
        if cnt + truck[0] > weight:
            q.append(0)
        else:
            x = truck.popleft()
            cnt += x
            q.append(x)
    
    return sec+bridge_length