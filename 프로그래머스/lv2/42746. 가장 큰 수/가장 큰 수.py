from functools import cmp_to_key

def comp(x,y):
    xy = str(x)+str(y)
    yx = str(y) + str(x)
    if xy > yx:
        return 1
    elif yx>xy:
        return -1
    else:
        return 0
    
def solution(numbers):
    answer = ''
    numbers.sort(key=cmp_to_key(comp), reverse=True)
    for i,c in enumerate(numbers):
        answer += str(c)
    answer = int(answer)
    return str(answer)