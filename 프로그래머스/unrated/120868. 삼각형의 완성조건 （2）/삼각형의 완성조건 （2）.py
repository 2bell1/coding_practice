import sys
sys.setrecursionlimit(5000)
def dfs(high, x, mid, answer, sidesis):
    if high < (x+mid) and high >= x and sidesis==True:  #sides 가 가장 긴 변
        dfs(high, x+1, mid, answer, sidesis)
        answer[0]+=1 
    elif high < (x+mid) and high >= x and sidesis==False: #나머지 한 변이 가장 긴 변
        dfs(high+1, x, mid, answer, sidesis)
        answer[0]+=1
    
    elif high > (x+mid) or high < x:
        return
    else:
        if sidesis == True:
            dfs(high, x+1, mid, answer, sidesis)
        else:
            dfs(high+1, x, mid, answer, sidesis)
        
def solution(sides):
    answer = [0]
    dfs(max(sides), (max(sides)-min(sides))+1, min(sides), answer, True)
    dfs(max(sides)+1, max(sides), min(sides), answer, False)
    print(max(sides), min(sides))
    return answer[0]