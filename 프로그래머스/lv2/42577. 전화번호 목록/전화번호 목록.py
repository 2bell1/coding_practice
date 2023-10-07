def solution(phone_book):
    answer = True
    arr={}
    for i,item in enumerate(phone_book):
        arr[item] = i
    sort_arr= sorted(arr.keys())
    for i,item in enumerate(sort_arr[:-1]):
        if item == sort_arr[i+1][:len(item)]:
            return False
        
    return answer