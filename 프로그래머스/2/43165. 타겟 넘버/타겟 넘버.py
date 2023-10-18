def dfs(numbers, i, tmp, pl,answer,target):
    
    if pl == True:
        tmp += numbers[i]
    else:
        tmp -= numbers[i]
    if i ==(len(numbers)-1):  # i가 리스트 길이와 같을 때 종료
        if tmp == target:
            print(tmp)
            answer[0] += 1
        return
    dfs(numbers, i+1,  tmp , True,answer,target)
    dfs(numbers, i+1,  tmp , False,answer,target)

def solution(numbers, target):
    answer = [0]
    dfs(numbers,0,0,True,answer,target)
    dfs(numbers,0,0,False,answer,target)
    return answer[0]