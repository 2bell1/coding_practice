from collections import deque

def route(maps, pos, target):
    rows, cols = len(maps), len(maps[0])
    # 방향: 아래, 오른쪽, 위, 왼쪽
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # 큐 초기화: 시작 위치와 경로 길이
    queue = deque([(pos[0], pos[1], 1)])  # (x, y, step)
    
    while queue:
        x, y, step = queue.popleft()

        # 목적지에 도달하면 바로 step 반환
        if [x, y] == target:
            return step

        # 4방향으로 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 유효한 범위 내에 있고, 벽이 아닌 곳이라면
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny, step + 1))
    
    # 도달할 수 없다면 -1 반환
    return -1

def solution(maps):
    pos = [0, 0]  # 시작점
    target = [len(maps) - 1, len(maps[0]) - 1]  # 목표점
    
    return route(maps, pos, target)
