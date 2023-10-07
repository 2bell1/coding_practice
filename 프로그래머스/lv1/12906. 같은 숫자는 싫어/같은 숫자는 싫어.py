from collections import deque
def solution(arr):
    answer = []
    check=deque()
    for c in arr:
        if not check or c != check[-1]:
            check.append(c)
            answer.append(c)
        
    return answer