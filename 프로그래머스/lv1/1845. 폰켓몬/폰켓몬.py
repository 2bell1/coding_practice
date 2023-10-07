def solution(nums):
    answer=0
    arr = {}
    
    for item in nums:
        if item in arr:
            arr[item]+=1
        else:
            arr[item]=1
    print(len(arr))
    if (len(nums)//2) >= len(arr):
        answer=len(arr)
    else:
        answer=len(nums)//2
    
    return answer