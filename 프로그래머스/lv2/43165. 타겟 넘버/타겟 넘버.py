from collections import deque
def solution(numbers, target):
    answer = 0
    deq = deque()
    deq.append([numbers[0],0])
    deq.append([-numbers[0],0])
    index=0
    while deq:
        tmp,index = deq.popleft()
        index+=1
        if index < len(numbers):
            deq.append([tmp+numbers[index], index])
            deq.append([tmp-numbers[index],index])
        else:
            if tmp == target:
                answer+=1
    return answer