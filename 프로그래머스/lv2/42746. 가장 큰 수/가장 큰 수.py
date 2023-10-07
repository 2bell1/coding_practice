from functools import cmp_to_key

# 우선순위를 설정하는 비교 함수 정의
def custom_sort(x, y):
    x_str, y_str = str(x), str(y)
    
    # x를 앞에 붙였을 때와 뒤에 붙였을 때의 값 계산
    x_with_prefix = int(x_str + y_str)
    x_with_suffix = int(y_str + x_str)
    
    # 두 값 중 더 큰 값을 반환하여 우선순위 설정
    if x_with_prefix > x_with_suffix:
        return 1
    elif x_with_prefix < x_with_suffix:
        return -1
    else:
        return 0
def solution(numbers):
    answer = ''
    str_numbers = [str(x) for x in numbers]
    str_numbers.sort(reverse=True,key=(cmp_to_key(custom_sort)))
    
    for i in str_numbers:
        answer+=i
    answer=int(answer)
    return str(answer)