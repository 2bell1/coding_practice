def solution(prices):
    size = len(prices)
    answer = [0] * size
    stack = []  # 스택에는 인덱스를 저장 (값이 아님!)

    for i in range(size):
        # 스택이 비어 있지 않고, 현재 값이 스택의 top보다 작으면 pop
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx  # 떨어지지 않은 기간 계산
        
        stack.append(i)  # 현재 인덱스를 스택에 저장

    # 끝까지 가격이 떨어지지 않은 경우 처리
    while stack:
        idx = stack.pop()
        answer[idx] = size - idx - 1  # 마지막까지 유지된 기간

    return answer
