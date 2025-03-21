from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque([[idx, pri] for idx, pri in enumerate(priorities)])
    pr = sorted(priorities)
    
    while dq:
        ans = dq.popleft()
        if ans[1] == pr[-1]:
            if ans[0] == location:
                return answer +1
            answer+=1
            pr.pop()
        else:
            dq.append(ans)
    
    return answer