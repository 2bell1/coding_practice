def solution(nums):
    answer = 0
    arr=set(nums)
    ln = len(arr)
    if (len(nums)/2) < ln:
        answer = (len(nums)/2)
    else:
        answer = ln
        
    return answer