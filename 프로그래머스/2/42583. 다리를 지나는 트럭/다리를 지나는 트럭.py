from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 위에 있는 트럭들의 현재 상태를 저장할 큐
    bridge = deque([0] * bridge_length)  # 다리 길이만큼 0으로 초기화
    bridge_w = 0  # 다리 위의 총 무게
    time = 0  # 경과 시간
    
    # 트럭 목록을 deque로 바꿈 (빠른 popleft 사용을 위해)
    truck_dq = deque(truck_weights)
    
    while truck_dq:
        time += 1  # 1초씩 경과
        
        # 다리 위에서 1초가 지나면 첫 번째 트럭이 다리를 떠남
        bridge_w -= bridge.popleft()
        
        # 트럭이 다리를 건널 수 있는지 확인
        if bridge_w + truck_dq[0] <= weight:
            # 트럭을 다리에 올림
            truck = truck_dq.popleft()  # 대기중인 트럭을 하나 꺼냄
            bridge.append(truck)  # 다리 위에 트럭을 올림
            bridge_w += truck  # 다리 위 총 무게에 추가
        else:
            # 트럭을 올릴 수 없으면 다리 위에서 1초가 지나가고, 트럭들은 이동
            bridge.append(0)  # 빈 공간을 다리에 추가
          
    # 모든 트럭이 다리를 건너면, 마지막으로 남은 트럭도 다리를 건너야 하므로 다리 길이만큼 추가 시간이 걸림
    return time + bridge_length
