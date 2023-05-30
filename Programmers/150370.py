#Programmers 150370번
#카카오 2023 

def solution(today, terms, privacies):
    answer = []
    alpha, num = [], []
    for i in range(len(terms)):
        a,n = terms[i].split()
        alpha.append(a)
        num.append(n)

    ttday = today.split('.')
    # today = int(ttday[0]+ttday[1]+ttday[2])
    ty,tm,td = int(ttday[0]), int(ttday[1]), int(ttday[2])
    
    for i in range(len(privacies)):
        day,a = privacies[i].split()
        index = alpha.index(a)
        month = int(num[index])
        
        dday = day.split('.')
        # day = int(dday[0]+dday[1]+dday[2])
        dy,dm,dd = int(dday[0]), int(dday[1]), int(dday[2])

        if dd == 1:
            dd = 28
            dm += month-1
            if dm > 12:
                dy += dm//12
                dm = dm%12
                if find(dy,dm,dd,ty,tm,td):
                    answer.append(i+1)
            else:
                if find(dy,dm,dd,ty,tm,td):
                    answer.append(i+1)
        else:
            dd -= 1
            dm += month
            if dm > 12:
                if dm % 12 == 0:
                    dy += dm//12-1
                    dm = 12
                else:
                    dy += dm//12
                    dm = dm%12
                if find(dy,dm,dd,ty,tm,td):
                    answer.append(i+1)
            else:
                if find(dy,dm,dd,ty,tm,td):
                    answer.append(i+1)
        
    return answer

def find(y,m,d,ty,tm,td):
    if y < ty:
        return True
    elif y == ty and m < tm:
        return True
    elif y == ty and m == tm and d < td:
        return True
    else:
        return False
    