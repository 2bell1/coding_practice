def solution(s):
    answer = []
    num,zeros=0,0
    
    
    while s != "1":
        zeros += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        num += 1
        
    answer.append(num)
    answer.append(zeros)
    return answer