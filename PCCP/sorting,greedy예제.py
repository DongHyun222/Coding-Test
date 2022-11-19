#PCCP시험대비 Sorting,greedy예제
#고속도로 경로 안에 최소 카메라 설치

def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    key = routes[0][1]

    for route in routes:
        if route[0] <= key and route[1] >= key:
            continue
        else:
            key = route[1]
            answer += 1

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

