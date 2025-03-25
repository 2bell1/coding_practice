from collections import deque

def solution(numbers):
    answer = [-1] * len(numbers)
    
    big = deque()
    big.appendleft(numbers[-1])
    for i in range(len(numbers)-2, -1, -1): #뒤에서부터 탐색
        
        if numbers[i] >= big[0]: # 현재 수가 뒷 큰수 스택 보다 클 시
            while big and numbers[i] >= big[0]:   # 스택 안의 현재 수보다 작은 수들 제거
                big.popleft()
            if big:  
                answer[i] = big[0] #제거 후 스택에 수가 있다면 제일 앞의 수가 뒷 큰수
            else:
                answer[i] = -1  # 스택이 비었다면 뒷 큰수가 없으므로 -1
            big.appendleft(numbers[i])  # 모두 제거 후 현재 수를 스택에 제일 앞에 삽입
            
        elif numbers[i] < big[0]: # 현재 수가 뒷 큰수 스택보다 작다면
            answer[i] = big[0]  # 스택의 제일 앞의 수가 뒷 큰수
            big.appendleft(numbers[i]) # 현재수를 바로 스택에 삽입
            
    return answer