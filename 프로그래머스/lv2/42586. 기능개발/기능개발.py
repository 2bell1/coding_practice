from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    success = deque()
    for i,c in enumerate(progresses):
        success.append(math.ceil((100-c)/speeds[i]))
    while success:
        count=1
        a=success.popleft()
        while success and a >= success[0]:
            success.popleft()
            count+=1
        answer.append(count)
    return answer