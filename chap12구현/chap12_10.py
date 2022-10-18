#기출문제
#구현10번 
#카카오 2020공채문제

# 2차원 리스트 90도 회전
def rotate_matrix_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

#자물쇠 중간값이 모두 1인지 확인
def check(new_lock):
    lock_lenth = len(new_lock) // 3
    for i in range(lock_lenth,lock_lenth * 2):
        for j in range(lock_lenth, lock_lenth * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    #기존 자물쇠 크기의 3배로 변환 후 중앙값 기존 자물쇠 넣음
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_matrix_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                #키를 자물쇠에 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] -= key[i][j]

    return False

