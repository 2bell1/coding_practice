from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0

    # 던전 순열을 모두 생성
    for order in permutations(dungeons, len(dungeons)):
        current_fatigue = k
        count = 0

        # 순서대로 던전을 탐험
        for min_fatigue, consume_fatigue in order:
            if current_fatigue >= min_fatigue:  # 던전 탐험이 가능한 경우
                current_fatigue -= consume_fatigue
                count += 1
            else:
                break  # 더 이상 탐험할 던전이 없으면 종료

        max_dungeons = max(max_dungeons, count)  # 최대 던전 수 업데이트

    return max_dungeons
