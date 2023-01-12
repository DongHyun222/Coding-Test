#백준 class3 7662번
#이중 우선순위 큐
#최대힙 최소힙 두개 만들고 키값을 활용해서 문제 해결
#너무 어렵다 여러번 풀어야될듯

import heapq

T = int(input())
for _ in range(T):
    K = int(input())
    max_heap, min_heap = [],[]
    visited = [False] * 1000001

    for key in range(K):
        word,num = input().split()

        if word == "I":
            heapq.heappush(min_heap, (int(num),key))
            heapq.heappush(max_heap, (int(num) * -1,key))
            visited[key] = True

        elif word == "D":
            if num == "-1": #최소값 삭제시 해당 노드가 다른힙에서 삭제된 노드인지 확인
                #이미 상대힙에 의해 삭제된 노드라면, 삭제되지 않은 노드가 나올때까지 계속 버림
                #이후 삭제대상노드가 나오면 삭제
                while min_heap and not visited[min_heap[0][1]]: #visited가 False이면 삭제된 상태
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False # 키값 False로 바꾸고 삭제
                    heapq.heappop(min_heap)
            elif num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
