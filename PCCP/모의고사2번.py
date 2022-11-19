import heapq
def solution(ability, number):          #이진힙을 통해 최소값 찾기
    answer = 0
    pQ = []
    for x in ability:
        heapq.heappush(pQ,x)

    for _ in range(number):             #최소값 두개 뽑아내서 합친후 다시 푸시
        min1 = heapq.heappop(pQ)
        min2 = heapq.heappop(pQ)
        heapq.heappush(pQ, min1+min2)
        heapq.heappush(pQ, min1+min2)

    answer = sum(pQ)
    return answer

print(solution([10, 3, 7, 2],2))

