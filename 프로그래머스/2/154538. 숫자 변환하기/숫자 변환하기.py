from collections import deque

def solution(x, y, n):
    # 큐에 (현재 값, 연산 횟수)를 넣어서 BFS 수행
    queue = deque([(x, 0)])
    
    # 방문한 값을 저장하여 중복 계산 방지
    visited = [False] * (y + 1)
    visited[x] = True
    
    while queue:
        current, steps = queue.popleft()

        # 목표 값에 도달하면 연산 횟수 반환
        if current == y:
            return steps
        
        # 가능한 연산을 모두 시도
        for next_val in [current + n, current * 2, current * 3]:
            if next_val <= y and not visited[next_val]:
                visited[next_val] = True
                queue.append((next_val, steps + 1))
            
    # 큐가 비면 y에 도달할 수 없는 경우
    return -1
