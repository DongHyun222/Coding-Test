##기출문제
##구현 7번 럭키스트레이트

N = input()
N_left = 0
N_right = 0
N_half = len(N) // 2

for i in range(len(N)):
    if i < N_half:
        N_left += int(N[i])
    else:
        N_right += int(N[i])

if N_left == N_right:
    print("LUCKY")
else:
    print("READY")