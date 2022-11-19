from collections import deque
def solution(menu, order, k):
    #menu[제조시간], order는 주문한 음료, k초 마다 새로운 손님옴
    answer = 0
    queue = deque()
    complete = -1       #음료를 만들수 있는지 확인
    idx = 0             #주문번호

    for t in range(k*(len(order)-1)+1):
        if t == complete:           #음료가 완성되면 큐에서 뺌
            queue.popleft()
            complete = -1
        if t == k*idx:              #k초마다 주문번호 큐에 넣음
            queue.append(order[idx])
            idx += 1
        if complete == -1 and len(queue) != 0:      #음료제조가능하면 제일 앞에있는거 제조
            complete = t + menu[queue[0]]
        
        answer = max(answer, len(queue))

    return answer

print(solution([5, 12, 30],	[1, 2, 0, 1],10))
