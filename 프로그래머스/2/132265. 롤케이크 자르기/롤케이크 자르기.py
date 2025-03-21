from collections import Counter
def solution(topping):
    answer = 0
    bro = Counter(topping)
    chul = set()
    for i in topping:
        if bro[i]:
            bro[i] -= 1
        if bro[i]==0:
            del bro[i]
        chul.add(i)
        if len(bro) == len(chul):
            answer += 1
    return answer