#PCCP모의고사 1번
#command를 통해 로봇 위치 설정

i = 0
def change(alpha):          #로봇 방향 회전
    global i                #i값을 기준으로 dxs,dys선택
    if alpha == 'R':
        i = (i+1) % 4
    else:
        i = (i+3) % 4

def solution(command):
    answer = [0,0]
    global i
    dx,dy = 0,0
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]

    for x in command:
        if x =='G':
            dx,dy = dx+dxs[i], dy+dys[i]
        elif x == 'B':
            dx,dy = dx-dxs[i], dy-dys[i]
        else:
            change(x)
    answer = [dx,dy]

    return answer

print(solution("GRGLGRG"))
