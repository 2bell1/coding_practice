def solution(s):
    answer = 0
    arr = []
    for i,char in enumerate(s):
        if(len(arr)==0):
            arr.append(char)
        elif arr[-1] == char:
            arr.pop()
        else:
            arr.append(char)
    if len(arr)==0:
        answer = 1
    
    return answer