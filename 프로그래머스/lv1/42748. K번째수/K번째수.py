def solution(array, commands):
    answer = []
    for index,(i,j,k) in enumerate(commands):
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer