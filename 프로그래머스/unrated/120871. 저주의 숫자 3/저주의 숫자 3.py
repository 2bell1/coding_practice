def solution(n):
    answer = 1
    i = 1
    num = 13
    if str(num) in "3":
        print(111)
    while 1:
        
        if (answer  % 3 ==0) or ("3" in str(answer)):
            answer +=1
            continue
        if i == n:
            break
        answer+=1
        i+=1
        
        
    return answer