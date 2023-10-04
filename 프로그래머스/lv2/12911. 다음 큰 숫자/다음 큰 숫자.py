def solution(n):
    target = bin(n)[2:].count('1')
    
    while 1:
        n +=1
        ans = bin(n)[2:].count('1')
        if(ans == target):
            break
        
    return n