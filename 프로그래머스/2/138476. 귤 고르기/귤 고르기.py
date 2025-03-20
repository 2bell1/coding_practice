from collections import Counter

def solution(k, tangerine):
    answer = 0
    many = Counter(tangerine)
    many_list = sorted(many.items(), key=lambda x: x[1], reverse=True)
    inside = 0
    for i in range(len(many_list)):
        answer += 1
        inside += many_list[i][1]
        if inside >= k:
            break
    return answer
