from collections import deque

def solution(order):
    answer = 0
    stack = deque()
    idx = 0  # order 리스트의 현재 인덱스
    size = len(order)

    for i in range(1, size + 1):
        if i == order[idx]:  # 컨베이어 벨트에서 바로 적재 가능
            answer += 1
            idx += 1
        else:
            stack.append(i)  # 보조 컨테이너에 보관

        # 스택의 맨 위가 현재 실어야 할 상자인지 확인하고, 맞으면 트럭에 적재
        while stack and stack[-1] == order[idx]:
            stack.pop()
            answer += 1
            idx += 1

    return answer
