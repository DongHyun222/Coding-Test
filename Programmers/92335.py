def prime(number):
    if number==1:
        return False
    for i in range(2, int(number**(0.5))+1):
        if number%i==0:
            return False
    return True

def solution(n, k):
    num=[]
    pb=''
    while n!=0:
        num.insert(0,n%k)
        n=n//k

    for x in num:
        pb+=str(x)

    spl=pb.split('0')
    spl=[int(i) for i in spl if i!=""]
    answer=0
    for x in spl:
        if prime(x):
            answer+=1
    return answer
print(solution(110011,10))