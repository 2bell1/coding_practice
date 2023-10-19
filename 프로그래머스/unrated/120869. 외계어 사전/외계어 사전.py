from collections import Counter
def solution(spell, dic):
    answer = 2
    ln = len(spell)
    counter={}
    for i, c in enumerate(dic):
        if len(c) != ln:
            continue
        else:
            counter= Counter(c)
            for a, b in enumerate(spell):
                if counter[b] != 1:
                    answer = 2
                    break
                else:
                    if a == (ln-1):
                        answer = 1
                        return answer
    return answer