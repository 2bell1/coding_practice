def solution(n):
    answer = 1
    i = 1
    while i<=n:
        
        if (answer  % 3 ==0) or ("3" in str(answer)):
            answer +=1
            continue
        if i == n:
            break
        answer+=1
        i+=1
        
        
    return answer
