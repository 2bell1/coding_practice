def solution(number, k):
    stack = []  # 정답을 만들기 위한 스택
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 이전 숫자가 현재 숫자보다 작으면 제거
            k -= 1
        stack.append(num)  # 현재 숫자를 스택에 추가

    # k개의 숫자를 다 제거하지 못한 경우(예: 54321 같은 경우)
    return ''.join(stack[:len(number)-k])
