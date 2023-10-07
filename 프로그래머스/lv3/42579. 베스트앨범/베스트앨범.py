def solution(genres, plays):
    answer = []
    arr={}
    sum_arr={}
    for i,(G,P) in enumerate(zip(genres,plays)):
        arr[(i,G)] = P
        if G in sum_arr:
            sum_arr[G] += P
        else:
            sum_arr[G] = P
    sum_arr=dict(sorted(sum_arr.items(),key= lambda x: -x[1]))
    print(sum_arr)
    arr=dict(sorted(arr.items(),key= lambda x: (-sum_arr[x[0][1]],-x[1],x[0][0])))
    count=1
    before=""
    for i,((index,G), P) in enumerate(arr.items()):
        if count>2 and before == G:
            continue
        if before != G:
            count = 1
            before=G
        answer.append(index)
        count+=1
            
    return answer