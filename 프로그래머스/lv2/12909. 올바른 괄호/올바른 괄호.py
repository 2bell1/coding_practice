def solution(s):
    answer = True
    neg=0;
    for char in s:
     if char=="(":
        neg+=1
     else:
        neg-=1
     if neg < 0:
            return False
        
    if neg!=0:  
            return False

    return True