def solution(babbling):
    answer = 0
    spk = {"aya", "ye", "woo", "ma"}
    
    for c in babbling:
        tmp = c
        for a in spk:
            tmp = tmp.replace(a," ")
        if tmp.isspace():
            answer+=1
    return answer