def solution(spell, dic):
    answer = 0
    for i, c in enumerate(dic):
        if not set(spell) - set(c):
            return 1
    return 2