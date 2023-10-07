def solution(clothes):
    answer = 1
    arr={}
    for i,(item,part) in enumerate(clothes):
        if part in arr:
            arr[part]+=1
        else:
            arr[part]=1
    for i,(part,num) in enumerate(arr.items()):
        answer*=(num+1)
    answer-=1
    return answer