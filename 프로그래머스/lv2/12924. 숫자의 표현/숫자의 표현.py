def solution(n):
    answer = 0
    i = 0
    sum=0
    minor=0
    while 1:
        if sum == n:
            answer+=1
        if(i == n):
            break
        i+=1 
        sum+=i
        if sum > n:
            while sum > n:
                minor+=1
                sum-=minor
        
    return answer